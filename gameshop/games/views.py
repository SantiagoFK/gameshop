# Games App Views

from django.shortcuts import render
from .models import Game

def gamelist(request):
    games = Game.objects.all()
    return render(request, 'games/gamelist.html', {'games': games})

