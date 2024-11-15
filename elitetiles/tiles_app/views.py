# tiles_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Tile , Profile, Category

# View for the homepage
def home(request):
    tiles = Tile.objects.all()  # Fetch all tiles
    return render(request, 'home.html', {'tiles': tiles})

# View for the product categories (floor, kitchen, bathroom, wall)
def category_view(request):  # Fetch tiles by category
    cata = Category.objects.all()
    return render(request, 'category.html',{'tiles': cata})

# View for the product details page
def product_detail(request, id):
    tile = Tile.objects.get(id=id)  # Get the tile by its id
    return render(request, 'product_detail.html', {'tile': tile})

# View for the sign-in page
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        phone_number = request.POST['contact']
        email = request.POST['address']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exists.')
            return render(request, 'signup.html')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('signin')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return render(request, 'signin.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            
            # Check if the user is admin with specific credentials
            if username == 'admin' and password == 'admin':
                return redirect('/admin/')  # Redirect to the admin page
            else:
                return redirect('home')  # Redirect to home for regular users
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'signin.html')


def cart(request):
    return render(request, 'cart.html')
def wishlist(request):
    return render(request, 'wishlist.html')
def about(request):
    return render(request,'about.html')


