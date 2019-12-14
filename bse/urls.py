from django.contrib import admin
from django.urls import include, path

from main.views import home

urlpatterns = [
    path('', home, name = 'home'),
    path('accounts/', include('accounts.urls'), name = 'accounts'),
    path('admin/', admin.site.urls, name = 'admin'),
]
