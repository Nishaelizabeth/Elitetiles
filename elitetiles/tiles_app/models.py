from django.db import models
from django.contrib.auth.models import User




class Tile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='tiles_images/')

    def __str__(self):
        return self.name

# Profile model to extend the User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.username} Profile'

