from django.urls import path
from . import views

urlpatterns = [
    path('reserve/<int:spot_id>/', views.reserve_spot, name='reserve_spot'),
    path('reservation-success/', views.reservation_success, name='reservation_success'),
    path('download-ticket/<int:reservation_id>/', views.download_ticket, name='download_ticket'),
]
