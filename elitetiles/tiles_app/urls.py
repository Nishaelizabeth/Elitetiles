from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # Homepage URL
    path('register/', views.register, name='signup'),
    path('login/', views.login_view, name='signin'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),  
    path('wishlist/', views.wishlist, name='wishlist'),
    path('category_view/', views.category_view, name='category_view'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
 # Category page
      # Product detail page
   #path('signin_view/',views.signin_view, name='signin_view'),
    #path('signup_view/',views.signup_view, name='signup_view'),
]
