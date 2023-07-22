# Api views

from django.shortcuts import render
from rest_framework import generics
from games.models import Game
from .serializers import GameSerializer

class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetailView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    




