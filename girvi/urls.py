from django.urls import path
from django.views.generic.dates import ArchiveIndexView

from . import views
from .models import Loan
urlpatterns = [
    path('', views.home, name='girvi-home'),
    path('loan_archive/',
         ArchiveIndexView.as_view(model=Loan, date_field="created"),
         name="loan_archive"),
    path('<int:year>/',
         views.LoanYearArchiveView.as_view(),
         name="loan_year_archive"),
    # Example: /2012/08/
    path('<int:year>/<int:month>/',
         views.LoanMonthArchiveView.as_view(month_format='%m'),
         name="archive_month_numeric"),
    # Example: /2012/aug/
    path('<int:year>/<str:month>/',
         views.LoanMonthArchiveView.as_view(),
         name="archive_month"),
    # Example: /2012/week/23/
    path('<int:year>/week/<int:week>/',
         views.LoanWeekArchiveView.as_view(),
         name="archive_week"),

    path('check/',views.check_girvi,name='check_girvi'),
    path('multirelease/', views.multirelease, name='girvi-multirelease'),

    path('bulk_release/',views.bulk_release,name='bulk_release'),
    path('bulk_release_detail/',views.bulk_release_detail,name='bulk_release_detail'),

    # urls for License
    path('license/', views.LicenseListView.as_view(),
         name='girvi_license_list'),
    path('license/create/', views.LicenseCreateView.as_view(),
         name='girvi_license_create'),
    path('license/detail/<int:pk>/',
         views.LicenseDetailView.as_view(), name='girvi_license_detail'),
    path('license/update/<int:pk>/',
         views.LicenseUpdateView.as_view(), name='girvi_license_update'),
    path('license/<int:pk>/delete/',
         views.LicenseDeleteView.as_view(), name='girvi_license_delete'),

    # urls for Loan
    path('loan/', views.LoanListView.as_view(), name='girvi_loan_list'),
    path('loan/manage/', views.manage_loans, name='manage_loans'),
    path('loan/renew/<int:pk>/', views.loan_renew, name='girvi_loan_renew'),
    path('loan/create/', views.LoanCreateView.as_view(),
         name='girvi_loan_create'),
    path('loan/<int:pk>/create/',
         views.LoanCreateView.as_view(), name='girvi_loan_create'),
    path('loan/detail/<int:pk>/',
         views.LoanDetailView.as_view(), name='girvi_loan_detail'),
    # path('girvi/loan/detail/<int:pk>/pdf',
    #      views.print_loanpledge, name='loan_pdf'),
    path('loan/update/<int:pk>/',
         views.LoanUpdateView.as_view(), name='girvi_loan_update'),
    path('loan/<int:pk>/delete/',
         views.LoanDeleteView.as_view(), name='girvi_loan_delete'),

    # urls for Adjustment
    path('adjustment/', views.AdjustmentListView.as_view(),
         name='girvi_adjustment_list'),
    path('adjustment/create/', views.AdjustmentCreateView.as_view(),
         name='girvi_adjustment_create'),
    path('adjustment/<int:pk>/create/',
         views.AdjustmentCreateView.as_view(), name='girvi_adjustment_create'),
    path('adjustment/update/<int:pk>/',
         views.AdjustmentUpdateView.as_view(), name='girvi_adjustment_update'),
    path('adjustment/<int:pk>/delete',
         views.AdjustmentDeleteView.as_view(), name='girvi_adjustment_delete'),


    # urls for series
    path('series/', views.SeriesListView.as_view(),
         name='girvi_series_list'),
    path('series/create/', views.SeriesCreateView.as_view(),
         name='girvi_series_create'),
    path('series/<int:pk>/create/',
         views.SeriesCreateView.as_view(), name='girvi_series_create'),
    path('series/detail/<int:pk>/',
         views.SeriesDetailView.as_view(), name='girvi_series_detail'),
    path('series/update/<int:pk>/',
         views.SeriesUpdateView.as_view(), name='girvi_series_update'),
    # path('series/<int:pk>/delete',
    #      views.SeriesDeleteView.as_view(), name='girvi_series_delete'),

    # urls for Release
    path('release/', views.ReleaseListView.as_view(),
         name='girvi_release_list'),
    path('release/create/', views.ReleaseCreateView.as_view(),
         name='girvi_release_create'),
    path('release/<int:pk>/create/',
         views.ReleaseCreateView.as_view(), name='girvi_release_create'),
    path('release/detail/<int:pk>/',
         views.ReleaseDetailView.as_view(), name='girvi_release_detail'),
    path('release/update/<int:pk>/',
         views.ReleaseUpdateView.as_view(), name='girvi_release_update'),
    path('release/<int:pk>/delete',
         views.ReleaseDeleteView.as_view(), name='girvi_release_delete'),

    # Example: /2012/week/23/
    path('notice/',
         views.notice,
         name="notice"),
]
