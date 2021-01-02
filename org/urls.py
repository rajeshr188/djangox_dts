from django.urls import path
from . import views

urlpatterns = [
    path('companies/',views.companylist,name = "org_company_list"),
    path('companies/add/',views.CompanyCreate.as_view(),name="org_company_create"),
    path('companies/members/',views.members,name = "org_members_list"),
    path('companies/members/add/',views.create_members,name = "org_members_create"),
    
    path('org/upgrade/',views.upgrade,name = "org_upgrade"),
    path('org/payment_method/',views.payment_method,name = 'org_payment_method'),
    path('org/card',views.card,name="org_card"),
]