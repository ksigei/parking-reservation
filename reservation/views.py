from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation
from parking.models import ParkingSpot
from datetime import datetime
from django.urls import reverse
from django.utils.timezone import now

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.text import slugify
from django.conf import settings
import os

@login_required
def reserve_spot(request, spot_id):
    spot = ParkingSpot.objects.get(id=spot_id)
    if spot.is_reserved:
        # Handle case where spot is already reserved
        pass
    else:
        # Handle reservation logic
        reservation = Reservation.objects.create(
            user=request.user,
            parking_spot=spot,
            start_time=now(),
            end_time=now()  # Add logic for end time
        )
        spot.is_reserved = True
        spot.save()
        # Redirect to payment page with the reservation ID
        return redirect(reverse('make_payment', args=[reservation.id]))

def reservation_success(request):
    pass
    return render(request, 'reservation_success.html')


def download_ticket(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    context = {'reservation': reservation}

    # Render ticket template to string
    ticket_html = render_to_string('ticket_template.html', context)

    # Generate unique filename for the ticket
    filename = f'ticket_{slugify(reservation.id)}.html'

    # Save ticket HTML to temporary directory
    ticket_path = os.path.join(settings.BASE_DIR, 'tmp', filename)
    with open(ticket_path, 'w') as ticket_file:
        ticket_file.write(ticket_html)

    # Read ticket HTML file and serve as downloadable attachment
    with open(ticket_path, 'rb') as ticket_file:
        response = HttpResponse(ticket_file.read(), content_type='text/html')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Remove temporary ticket file
    os.remove(ticket_path)

    return response
