from django.shortcuts import render
from .models import Customer
from .tables import CustomerTable
from .filters import CustomerFilter
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
# Create your views here.


@login_required
def home(request):
    data = dict()
    c = Customer.objects
    data['retailcount'] = c.filter(type='Re').count()

    data['wol'] = c.filter(type='Re', loan=None).count()
    data['wl'] = data['retailcount']-data['wol']
    data['customercount'] = c.all().count()

    data['whcount'] = c.filter(type="Wh").count()
    try:
        data['withph'] = round(
            (c.exclude(phonenumber='911').count()/c.count() or 1)*100, 2)
    except:
            data['withph'] = None
    data['religionwise'] = c.values('religion').annotate(
        Count('religion')).order_by('religion')

    return render(request, 'contact/home.html', context={'data': data},)


class CustomerListView(LoginRequiredMixin, ExportMixin, SingleTableMixin, FilterView):
    table_class = CustomerTable
    model = Customer
    template_name = 'contact/customer_list.html'
    filterset_class = CustomerFilter
    paginate_by = 25


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('contact_customer_list')


def reallot_receipts(request, pk):
    customer = Customer.objects.get(pk=pk)
    customer.reallot_receipts()
    return redirect(customer.get_absolute_url())


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # data = self.object.sales.all()
        # table = InvoiceTable(data, exclude=('customer', 'edit', 'delete',))
        # table.paginate(page=self.request.GET.get('page', 1), per_page=25)
        # context['invoices'] = table

        # inv = data.exclude(status="Paid")
        # how_many_days = 30
        # context['current'] = inv.filter(created__gte=datetime.now()-timedelta(days=how_many_days)).aggregate(
        #     tc=Sum('balance', filter=Q(balancetype='Cash')), tm=Sum('balance', filter=Q(balancetype='Metal')))
        # context['past'] = inv.filter(created__lte=datetime.now()-timedelta(days=how_many_days)).aggregate(
        #     tc=Sum('balance', filter=Q(balancetype='Cash')), tm=Sum('balance', filter=Q(balancetype='Metal')))
        # context['monthwise'] = inv.annotate(month=Month('created')).values('month').order_by('month').annotate(tc=Sum(
        #     'balance', filter=Q(balancetype='Cash')), tm=Sum('balance', filter=Q(balancetype='Metal'))).values('month', 'tm', 'tc')
        # context['monthwiserev'] = data.annotate(month=Month('created')).values('month').order_by('month').annotate(tc=Sum(
        #     'balance', filter=Q(balancetype='Cash')), tm=Sum('balance', filter=Q(balancetype='Metal'))).values('month', 'tm', 'tc')
        return context


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm


class CustomerDelete(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('contact_customer_list')
