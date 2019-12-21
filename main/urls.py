from django.urls import path

from .views import home, edu_info, company_info

urlpatterns = [
    path('', home, name='home'),
    path('edu_plan/', edu_info),
    path('company_info/', company_info)
]
