from contact.models import Customer
from django.contrib import admin
# from django import forms
# from import_export import fields, resources
# from import_export.admin import ImportExportActionModelAdmin
from .models import Customer
# # Register your models here.
# class CustomerResource(resources.ModelResource):
    
#     class Meta:
#         model=Customer

# class CustomerAdminForm(forms.ModelForm):

#     class Meta:
#         model = Customer
#         fields = '__all__'

# class CustomerAdmin(ImportExportActionModelAdmin):
#     form = CustomerAdminForm
#     resource_class=CustomerResource
#     list_display = ['name', 'id', 'created', 'last_updated', 'phonenumber', 'Address','area', 'type', 'relatedas', 'relatedto']
#     readonly_fields = ['name', 'id', 'created', 'last_updated', 'phonenumber', 'Address', 'area','type', 'relatedas', 'relatedto']

# admin.site.register(Customer, CustomerAdmin)
admin.site.register(Customer)