
class Cart():
    def __init__(self, request):
        self.session = request.session

        #get the current session key if it exist
        cart = self.session.get('session_key')

        # if the user is new, no session key, crearte one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # make sure cart is available on all page of site
        self.cart = cart 