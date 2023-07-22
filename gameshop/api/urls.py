# Api urls

from django.urls import path
from . import views

urlpatterns = [
    path('games', views.GameListView.as_view(), name='game_list'),
    path('games/<int:pk>', views.GameDetailView.as_view(), name='game_detail'),
]