from django.test import TestCase, Client
from django.urls import reverse
from .models import Reservation
from parking.models import ParkingSpot
from user_auth.models import CustomUser
from datetime import datetime, timedelta
from django.utils import timezone

class ReserveSpotViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='test_user', email='testmain@mail.test', password='test_password')
        self.spot = ParkingSpot.objects.create(spot_number='32324t', is_reserved=False, fee=10)
        self.spot_id = self.spot.id

    def test_reserve_spot_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('reserve_spot', args=[self.spot_id]))
        self.assertEqual(response.status_code, 302)  

    def test_reserve_spot_post(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('reserve_spot', args=[self.spot_id]))
        reservation = Reservation.objects.last()
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(reservation)
        self.assertEqual(reservation.user, self.user)
        self.assertEqual(reservation.parking_spot, self.spot)
        self.assertTrue(reservation.start_time)
        self.assertTrue(reservation.end_time)

class DownloadTicketViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='test_user', email='testmain@mail.test', password='test_password')
        self.spot = ParkingSpot.objects.create(spot_number='32324t', is_reserved=False, fee=10)
        self.reservation = Reservation.objects.create(user=self.user, parking_spot=self.spot, start_time=timezone.now(), end_time=timezone.now() + timedelta(hours=1))
        self.reservation_id = self.reservation.id

    def test_download_ticket(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('download_ticket', args=[self.reservation_id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
