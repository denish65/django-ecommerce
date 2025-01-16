from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product

def home(request):

    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})
    # return render(request, 'products/base.html', {'products': products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})
from django.shortcuts import redirect
from .models import Cart, CartItem

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


def cart(request):
    # Dummy cart data; replace with real logic
    cart_items = [
        {'name': 'Product 1', 'quantity': 2, 'price': 100},
        {'name': 'Product 2', 'quantity': 1, 'price': 200},
    ]
    return render(request, 'product/cart.html', {'cart_items': cart_items})

def checkout(request):
    return render(request, 'product/checkout.html')

def category(request, category):
    products = Product.objects.filter(category__icontains=category)
    return render(request, 'product/category.html', {'products': products, 'category': category})