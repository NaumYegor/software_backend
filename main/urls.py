from django.urls import path

from .views import home, edu_info, company_info, our_team

urlpatterns = [
    path('', home, name='home'),
    path('edu_plan/', edu_info),
    path('company_info/', company_info),
    path('our_team/', our_team)
]
