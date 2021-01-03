from django.urls import path
from . import views

urlpatterns = (
    # urls for Customer
    path('', views.home, name='contact_home'),
    path('list/', views.CustomerListView.as_view(),
         name='contact_customer_list'),
    path('create/', views.CustomerCreateView.as_view(),
         name='contact_customer_create'),
    path('detail/<int:pk>/', views.CustomerDetailView.as_view(),
         name='contact_customer_detail'),
    path('update/<int:pk>/', views.CustomerUpdateView.as_view(),
         name='contact_customer_update'),
    path('delete/<int:pk>/', views.CustomerDelete.as_view(),
         name='contact_customer_delete'),
#     path('customer/<int:pk>/reallot/', views.reallot_receipts,
#          name='contact_reallot_receipts')
)
