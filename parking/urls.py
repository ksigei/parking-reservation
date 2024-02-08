from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_parking_spots, name='list_parking_spots'),
]