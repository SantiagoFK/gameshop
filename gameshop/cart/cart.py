'''
Cart needs to be stored on each session, even if a user is not logged in. Then if the user
logs in, the cart info needs to be passed to the current session.

Cart uses a dictionary, where the key is the game id and the value is an object with fields:
quantity and price.
'''


from games.models import Game
from django.conf import settings

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, game, quantity=1, override_quantity=False):
        '''
        add a game to the cart or update its quantity
        '''
        
        # has to be string because session info will later map to JSON data
        game_id = str(game.id)
        if game_id not in self.cart:
            self.cart[game_id] = {
                'quantity': 0,
                'price': str(game.price)
            }
        
        if override_quantity:
            self.cart[game_id]['quantity'] = quantity
        else:
            self.cart[game_id]['quantity'] += quantity
        
        self.save()
    
    def save(self):
        # mark the session as 'modified' to make sure it's saved
        self.session.modified = True