# tiles_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Tile

# View for the homepage
def home(request):
    tiles = Tile.objects.all()  # Fetch all tiles
    return render(request, 'home.html', {'tiles': tiles})

def signin_view(request):
    return render(request, 'signin.html')

def signup_view(request):
    return render(request, 'signup.html')

# View for the product categories (floor, kitchen, bathroom, wall)
def category(request, category):
    tiles = Tile.objects.filter(category=category)  # Fetch tiles by category
    return render(request, 'category.html', {'tiles': tiles})

# View for the product details page
def product_detail(request, id):
    tile = Tile.objects.get(id=id)  # Get the tile by its id
    return render(request, 'product_detail.html', {'tile': tile})

# View for the sign-in page
def signin(request):
    # If the method is POST, attempt to authenticate the user
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If the user exists, log them in and redirect to home
            login(request, user)
            return redirect('home')
        else:
            # If authentication fails, return an error message
            return HttpResponse("Invalid credentials. Please try again.")

    # If it's a GET request, render the sign-in page
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        contact = request.POST['contact']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Validate password confirmation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        # Create a new user
        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=firstname,
                last_name=lastname
            )
            user.profile.address = address  # Assuming you have a user profile model for storing address, contact, etc.
            user.profile.contact = contact
            user.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('signin')
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return redirect('signup')
    
    return render(request, 'signup.html')

def cart(request):
    return render(request, 'cart.html')
def wishlist(request):
    return render(request, 'wishlist.html')
def about(request):
    return render(request,'about.html')

