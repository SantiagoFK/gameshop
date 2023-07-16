# Games App Urls

from django.urls import path
from .views import gamelist, gamedetail

urlpatterns = [
    path('', gamelist, name='gamelist'),
    path('<int:id>/', gamedetail, name='gamedetail'),
]