from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.timezone import now
from django.http import HttpResponse, HttpResponseServerError
from django.utils.text import slugify
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from .models import Reservation
from parking.models import ParkingSpot

@login_required
def reserve_spot(request, spot_id):
    spot = ParkingSpot.objects.get(id=spot_id)
    if spot.is_reserved:
        pass
    else:
        # cereate reservation 
        reservation = Reservation.objects.create(
            user=request.user,
            parking_spot=spot,
            start_time=now(),
            end_time=now()  
        )
        spot.is_reserved = True
        spot.save()
        # redirect to payment page with the reservation ID
        return redirect(reverse('make_payment', args=[reservation.id]))

def reservation_success(request):
    pass
    return render(request, 'reservation_success.html')


@login_required
def download_ticket(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    # create ticket in pdf format
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ticket_{slugify(reservation.id)}.pdf"'

    try:
        # pdf
        doc = SimpleDocTemplate(response, pagesize=letter)
        styles = getSampleStyleSheet()
        
        header_text = Paragraph("<b>Reservation Ticket</b>", styles['Heading1'])
        contacts_text = Paragraph("<b>Contact Information:</b><br/>Email: admin@reservaton.com<br/>Phone: +1234567890", styles['Normal'])

        footer_text = Paragraph("Thank you for your reservation", styles['Normal'])

        # content
        ticket_content = [
            header_text,
            Spacer(1, 12),
            Paragraph(f"<b>Reservation ID:</b> {reservation.id}", styles['Normal']),
            Spacer(1, 12),
            Paragraph(f"<b>User:</b> {reservation.user}", styles['Normal']),
            Spacer(1, 12),
            Paragraph(f"<b>Parking Spot:</b> {reservation.parking_spot}", styles['Normal']),
            Spacer(1, 12),
            Paragraph(f"<b>Start Time:</b> {reservation.start_time}", styles['Normal']),
            Spacer(1, 12),
            Paragraph(f"<b>End Time:</b> {reservation.end_time}", styles['Normal']),
            Spacer(1, 12),
            contacts_text,
            Spacer(1, 12),
            footer_text
        ]

        # building pdf
        doc.build(ticket_content)

        return response
    except Exception as e:
        return HttpResponseServerError("Failed to generate ticket. Please try again later.")


