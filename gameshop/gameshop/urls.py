# Main Urls

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('games.urls', namespace='games')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('account/', include('accounts.urls')),
    path('api/', include('api.urls')),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
