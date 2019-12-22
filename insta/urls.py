from django.urls import path

from .views import recent_photos

urlpatterns = [
    path('recent/', recent_photos, name='recent_photos')
]
