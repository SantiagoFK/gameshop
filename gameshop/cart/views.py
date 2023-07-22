# Cart App views

from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from games.models import Game
from .forms import CartAddGameForm

@require_POST
def cart_add(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    form = CartAddGameForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(game=game,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    cart.remove(game)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    
    for item in cart:
        item['update_quantity_form'] = CartAddGameForm(initial={
            'quantity': item['quantity'],
            'override': True})
        
    return render(request, 'cart/detail.html', {'cart': cart})