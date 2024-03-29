"""Views for all the cart function"""
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from store.models import Product
from .cart import Cart



def cart_summary(request):
    """Summary of the cart"""
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart_summary.html",
                  {"cart_products":cart_products,
                   "quantities":quantities,
                   "totals":totals})

def cart_add(request):
    """Function for adding the items in cart"""
    #Get the cart
    cart = Cart(request)

    #Test for post
    if request.POST.get('action') == 'post':
        #Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # Look product in DB
        product = get_object_or_404(Product, id=product_id)

        # Save to session
        cart.add(product=product, quantity=product_qty)

        # Get cart quantity
        cart_quantity = cart.__len__()

        # Return response
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Product added to cart..."))
        return response

def cart_delete(request):
    """Delete items in cart"""
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #Get stuff
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})
        messages.success(request, ("Item deleted from shopping cart..."))
        return response


def cart_update(request):
    """Update items in the shopping Cart"""
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        messages.success(request, ("Your cart has been Updated..."))
        return response
