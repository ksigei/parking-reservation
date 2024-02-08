from django.shortcuts import render, redirect
from .models import Payment
from reservation.models import Reservation

def make_payment(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    amount = reservation.parking_spot.fee  
    if request.method == 'POST':
        
        # Create a new Payment object
        Payment.objects.create(
            reservation=reservation,
            amount=amount,
            payment_status='Paid' 
        )

        return render(request, 'payment_success.html', {'reservation': reservation})

    context = {
        'reservation': reservation,
        'amount': amount
    }
    return render(request, 'make_payment.html', context)
