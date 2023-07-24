# Orders App views

from django.shortcuts import render
from .models import OrderItem
from cart.cart import Cart
from .forms import OrderCreateForm

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         game=item['game'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            
            # clear the cart
            cart.clear()
            
            return render(request,
                          'orders/order_success.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    
    return render(request,
                  'orders/order_create.html',
                  {'cart': cart, 'form': form})





