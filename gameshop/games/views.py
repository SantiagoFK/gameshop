# Games App Views

from django.shortcuts import render
from django.http import Http404

from .models import Game

def gamelist(request):
    games = Game.objects.all()
    return render(request, 'games/gamelist.html', {'games': games})


def gamedetail(request, id):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        raise Http404('No such game in the database.')

    return render(request, 'games/gamedetail.html', {'game': game})

# this can be written with the get_object_or_404 shortcut.