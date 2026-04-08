from django.urls import path
from . import views

urlpatterns = [
    path('api/entries/', views.api_entries, name='api_entries'),
]