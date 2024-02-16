from django.test import TestCase, Client
from django.utils import timezone
from user_auth.models import CustomUser as User
from django.urls import reverse
from reservation.models import Reservation, ParkingSpot
from payment.models import Payment
from payment.views import make_payment

class MakePaymentViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='testmain@mail.test', password='test_password')
        self.client = Client()
        start_time = timezone.now()
        end_time = start_time + timezone.timedelta(hours=1) 
        self.parking_spot = ParkingSpot.objects.create(fee=10) 
        self.reservation = Reservation.objects.create(user=self.user, start_time=start_time, end_time=end_time, parking_spot=self.parking_spot) 

    def test_make_payment_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('make_payment', args=[self.reservation.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'make_payment.html')

    def test_make_payment_post(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('make_payment', args=[self.reservation.id]))
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'payment_success.html')
