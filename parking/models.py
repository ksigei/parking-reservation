from django.db import models

class ParkingSpot(models.Model):
    spot_number = models.CharField(max_length=50, unique=True)
    is_reserved = models.BooleanField(default=False)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.spot_number
