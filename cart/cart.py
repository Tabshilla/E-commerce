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
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        #Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

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

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        #get cart
        ourcart = self.cart
        #update the cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        test = self.cart
        return test

    def delete(self, product):
        product_id = str(product) # {'4' : 2}
        #delete from dictionary
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True


