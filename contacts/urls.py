from django.urls import path
from .views import ContactList,ContactCreate

urlpatterns = [
    path('contacts/',ContactList.as_view(),name= 'org_contact_list'),
    path('contacts/add/',ContactCreate.as_view(),name='org_contact_add')
]