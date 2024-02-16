from django.test import TestCase
from django.urls import reverse
from .models import ParkingSpot
from .views import list_parking_spots

class ParkingSpotTestCase(TestCase):
    def setUp(self):
        self.spot = ParkingSpot.objects.create(spot_number='323232e', is_reserved=False, fee=10.00)

    def test_parking_spot_creation(self):
        self.assertEqual(self.spot.spot_number, '323232e')
        self.assertEqual(self.spot.is_reserved, False)
        self.assertEqual(self.spot.fee, 10.00)

class ParkingSpotViewTestCase(TestCase):
    def setUp(self):
        self.spot = ParkingSpot.objects.create(spot_number='323232e', is_reserved=False, fee=10.00)

    def test_list_parking_spots(self):
        response = self.client.get(reverse('list_parking_spots'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parking_spots.html')
        self.assertContains(response, self.spot.spot_number)
