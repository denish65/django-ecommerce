from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('products', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    # path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('category/<str:category>/', views.category, name='category'),
]
