# Games App Urls

from django.urls import path
from .views import gamelist

urlpatterns = [
    path('', gamelist, name='gamelist'),
]