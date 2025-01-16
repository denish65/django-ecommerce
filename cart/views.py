# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Cart, CartItem
from products.models import Product

def add_to_cart(request, product_id):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=product_id)
    cart_item, _ = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, 'cart/cart_detail.html', {'cart': cart})
