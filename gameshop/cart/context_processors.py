# context_processor to make the cart object available to all views.

from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}