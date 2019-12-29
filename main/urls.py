from django.urls import path

from .views import home, edu_info, company_info, our_team, article

urlpatterns = [
    path('', home, name='home'),
    path('our_team/', our_team),
    path('news/<int:article_id>', article),
    path('edu_plan/', edu_info),
    path('company_info/', company_info)
]
