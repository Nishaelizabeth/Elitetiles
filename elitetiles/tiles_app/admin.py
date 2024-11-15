# admin.py
from django.contrib import admin
from .models import Tile, Profile, Category

# Register the Tile model
@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description', 'image')  # Display these fields in the list view
    search_fields = ('name', 'category__name')  # Search functionality for name and category name
    list_filter = ('category',)  # Filter by category

# Register the Profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'contact')  # Display user, address, and contact in the list view
    search_fields = ('user__username', 'address')  # Search by username and address

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','image')  # Display category name in the list view
    search_fields = ('name',)  # Search functionality for category name
