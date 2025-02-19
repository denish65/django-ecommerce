from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem, Order
from django.contrib.auth.decorators import login_required
import sys

def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=product_id)
    
    cart_item, _ = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, 'products/cart_detail.html', {'cart': cart})

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        cart_item.delete()  # Remove the item from the cart
        return redirect('cart_detail')  # Redirect to the cart detail page

# @login_required
def checkout(request):
    order_items = []  # Initialize order_items
    total = 0  # Initialize total

    if request.method == 'POST':
        selected_items = request.POST.getlist('selected_items')  # Get selected item IDs
        print(selected_items)  # Debugging output

        for item_id in selected_items:
            cart_item = get_object_or_404(CartItem, id=item_id)
            total += cart_item.product.price * cart_item.quantity
            order_items.append(cart_item)  # Add item to order items
            cart_item.delete()  # Remove item from cart after checkout

        # Create an order
        order = Order.objects.create(user=request.user, total=total)

        return redirect('checkout')  # Redirect to checkout page to show confirmation

    cart = Cart.objects.filter(user=request.user).first()
    return render(request, 'products/checkout.html', {'cart': cart, 'order_items': order_items, 'total': total})

def category(request, category):
    products = Product.objects.filter(category__icontains=category)
    return render(request, 'products/category.html', {'products': products, 'category': category})

# @login_required
def order_list(request):
    # Retrieve all orders for the logged-in user
    orders = Order.objects.filter(user=request.user)
    return render(request, 'products/order_list.html', {'orders': orders})