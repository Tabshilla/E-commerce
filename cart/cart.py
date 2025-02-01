from Ecom_store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        #get request
        self.request = request

        #Get current session key if it exists
        cart = self.session.get('session_key')

        #If no cart exists, start a new one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make sure the cart is available on all the pages in the site
        self.cart = cart
    
    def add(self, product):
        product_id = str(product.id)

        #Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        #get ids from cart
        product_ids = self.cart.keys()

        #use ids to lookup products
        products = Product.objects.filter(id__in=product_ids)
        #return thodse products
        return products