from django.urls import path
from.import views
urlpatterns = [
    path('', views.home, name='dea_home'),
    path('accounts/',views.AccountListView.as_view(), name = "dea_account_list"),
    path('account/<int:pk>/',views.AccountDetailView.as_view(), name = "dea_account_detail"),
    path('account/add/', views.AccountCreateView.as_view(), name = 'dea_Account_create'),
    
    
]
