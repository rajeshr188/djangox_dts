from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,DetailView
from django.shortcuts import render
# Create your views here.
from . import models

def home(request):
    context={}
    context['accounts'] = models.Account.objects.all()
    context['ledger'] = models.Ledger.objects.all()
    return render(request,'dea/home.html',{'data':context})

class AccountCreateView(CreateView):
    model = models.Account

class AccountListView(ListView):
    model = models.Account

class AccountDetailView(DetailView):
    model = models.Account