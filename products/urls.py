from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='products'),
    path('home', views.home, name='products'),

    path('products', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_list, name='order_list'),
    path('category/<str:category>/', views.category, name='category'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
