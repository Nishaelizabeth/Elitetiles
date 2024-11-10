from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),  
    path('wishlist/', views.wishlist, name='wishlist'),
    path('category/<str:category>/', views.category, name='category'),  # Category page
    path('product/<int:id>/', views.product_detail, name='product_detail'),  # Product detail page
    path('signin_view/',views.signin_view, name='signin_view'),
    path('signup_view/',views.signup_view, name='signup_view'),
]
