from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('parking.urls')),
    path('user/', include('user_auth.urls')),
    path('reservation/', include('reservation.urls')),
    path('payment/', include('payment.urls')),
    path('notification/', include('notification.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
