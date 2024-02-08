from django.shortcuts import render
from .models import ParkingSpot

def list_parking_spots(request):
    parking_spots = ParkingSpot.objects.all()
    return render(request, 'parking_spots.html', {'parking_spots': parking_spots})
