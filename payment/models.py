from django.db import models
from reservation.models import Reservation

class Payment(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20)  # Pending, Paid, Failed, etc.

    def __str__(self):
        return f"{self.reservation} - {self.amount}"
