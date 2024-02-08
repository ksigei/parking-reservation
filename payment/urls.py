from django.urls import path
from . import views

urlpatterns = [
    path('pay/<int:reservation_id>/', views.make_payment, name='make_payment'),
]
