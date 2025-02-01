from django.shortcuts import render, get_object_or_404
from .cart import Cart
from Ecom_store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    #Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    return render(request, "cart_summary.html", {"cart_products": cart_products})


def cart_add(request):
    #get cart
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') == 'post':

        #get prduct
        product_id = int(request.POST.get('product_id'))
        #look up product in the db
        product = get_object_or_404(Product, id=product_id)


        #save to a session
        cart.add(product=product)

        #Get cart quantity
        cart_quantity = cart.__len__()
        


        #return a json response
        # response = JsonResponse({'Product Name :' : product.name})
        response = JsonResponse({'qty :' : cart_quantity})
        return response


def cart_delete(request):
    pass


def cart_update(request):
    pass