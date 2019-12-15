from django.urls import path

from .views import sign_in, logout, registration, restore_password

urlpatterns = [
    path('sign_in/', sign_in, name='sign_in'),
    path('logout/', logout, name='logout'),
    path('registration/', registration, name='registration'),
    path('restore_password/', restore_password, name= 'restore_password')
]
