from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('main.urls'), name='main'),
    path('insta/', include('insta.urls'), name='insta'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('admin/', admin.site.urls, name='admin'),
]
