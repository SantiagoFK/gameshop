# Games App Views

from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddGameForm


from .models import Game

def gamelist(request):
    games = Game.objects.all()
    return render(request, 'games/gamelist.html', {'games': games})


def gamedetail(request, id):
    game = get_object_or_404(Game, id=id)
    cart_game_form = CartAddGameForm()

    return render(request, 'games/gamedetail.html', {'game': game, 
                                                     'cart_game_form': cart_game_form})
