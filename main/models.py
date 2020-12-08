from django.db import models

# Create your models here.


class Pizza(models.Model):
    pizza_type = (
        ('Regular', 'Regular'),
        ('Square', 'Square'),
    )
    size = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )
    topping = (
        ('Onion', 'Onion'),
        ('Tomato', 'Tomato'),
        ('Corn', 'Corn'),
    )
    name = models.CharField(max_length=200)
    pizza_types = models.CharField(
        max_length=200, null=True, choices=pizza_type)
    pizza_size = models.CharField(max_length=200, null=True, choices=size)
    topping = models.CharField(max_length=200, null=True, choices=topping)

    def __str__(self):
        return self.name
