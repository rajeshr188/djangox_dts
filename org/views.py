from django.forms import fields
from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic import CreateView,ListView
from .models import Company
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import Group
from accounts.forms import CustomUserCreationForm
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
import stripe
from config import settings
# Create your views here.

API_KEY = settings.STRIPE_SECRET_KEY

def change_schema(request):
    return render(request,'pages/home.html')

@permission_required('org.view_company', raise_exception=True)
@login_required
def companylist(request):
    paid = False
    is_owner = False
    if request.user.is_anonymous:
        c = 'Public'
    elif request.user.company:
        c= request.user.company.name
        paid = request.user.company.has_paid()
        is_owner = request.user.groups.filter(name='tenant_owner').exists()
    else:
        c = 'None'
        
    return render(request,'org/company_list.html',{'c':c,'paid':paid,'is_owner':is_owner,})


@permission_required('org.view_company', raise_exception=True)
@login_required
def members(request):
    members = request.user.company.customuser_set.all()
    is_owner = request.user.groups.filter(name='tenant_owner').exists()
    print(members)
    return render(request,'org/members.html',{'members':members,'is_owner':is_owner})


@permission_required('accounts.add_customuser', raise_exception=True)
@login_required
def create_members(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomUserCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user = form.save()
            user.is_staff = True
            user.company = request.user.company
            user.groups.clear()
            group = Group.objects.get(name='tenant_staff')
            group.user_set.add(user)
            user.save()
            return HttpResponseRedirect('/orgs/companies/members/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserCreationForm()

    return render(request, 'org/create_members.html', {'form': form})

class CompanyCreate(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    permission_required = 'org.add_company'
    model = Company
    success_url = reverse_lazy("home")
    fields = ['domain_url', 'name','schema_name', 'paid_untill', 'on_trial']
    
    def form_valid(self,form):
        company = form.save()
        self.request.user.company = company
        self.request.user.save()
        return super(CompanyCreate,self).form_valid(form)

@login_required
def upgrade(request):

    return render(request, 'org/upgrade.html')

@require_POST
@login_required
def payment_method(request):
    stripe.api_key = API_KEY
    plan = request.POST.get('plan','m')
    auto_renewal = request.POST.get('auto_renewal',True)
    payment_gateway = request.POST.get('payment_gateway','card')
    context ={}
    print(settings.STRIPE_PUBLISHABLE_KEY)
    payment_intent = stripe.PaymentIntent.create(
        amount = 999,
        currency = 'inr',
        payment_method_types = ['card']
    )

    if payment_gateway == 'card':
        context['SECRET_KEY'] = payment_intent.client_secret
        context['PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY
        context['customer_email'] = request.user.email
        context['payment_intent_id'] = payment_intent.id
    return render(request,'org/card.html',context)

@login_required
def card(request):

    payment_intent_id = request.POST['payment_intent_id']
    payment_method_id = request.POST['payment_method_id']
    print(payment_intent_id,payment_method_id)
    return render(request,'org/thank_you.html')
