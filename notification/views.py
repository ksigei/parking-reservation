from django.shortcuts import render
from .models import Notification

def list_notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'list_notifications.html', {'notifications': notifications})

