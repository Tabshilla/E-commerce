from django.shortcuts import render, get_object_or_404
from .cart import Cart
from Ecom_store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    #Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals})


def cart_add(request):
    #get cart
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') == 'post':

        #get prduct
        product_id = int(request.POST.get('product_id'))
        product_qty= int(request.POST.get('product_qty'))
        #look up product in the db
        product = get_object_or_404(Product, id=product_id)


        #save to a session
        cart.add(product=product, quantity=product_qty)

        #Get cart quantity
        cart_quantity = cart.__len__()
        


        #return a json response
        # response = JsonResponse({'Product Name :' : product.name})
        response = JsonResponse({'qty :' : cart_quantity})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        #delete 
        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty= int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        return response
        # return redirect('cart_summary')