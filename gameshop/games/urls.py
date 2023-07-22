# Games App Urls

from django.urls import path
from .views import gamelist, gamedetail

app_name = 'games'

urlpatterns = [
    path('', gamelist, name='gamelist'),
    path('<int:id>/', gamedetail, name='gamedetail'),
]