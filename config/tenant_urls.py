from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    # path('contacts/', include('contacts.urls')),
    path('orgs/', include('org.urls')),
    path('dea/',include('dea.urls')),
    path('contact/',include('contact.urls')),
    path('girvi/',include('girvi.urls')),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
