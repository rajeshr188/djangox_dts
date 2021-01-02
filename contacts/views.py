from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# Create your views here.
class ContactList(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = 'contacts.view_contact'
    model = Contact


class ContactDetail(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = 'contacts.view_contact'
    model = Contact


class ContactCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'contacts.add_contact'
    model = Contact
    success_url = reverse_lazy("org_contact_list")
    fields =['name','phoneno']
