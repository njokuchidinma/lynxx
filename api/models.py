from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser


# Create your models here.
USERS = [
    ("admin", "ADMIN"), 
    ("staff", "STAFF"),
    ("customer", "CUSTOMER"),
]
GENDER = [
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ]

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=15, choices=GENDER, default="female")
    date_of_birth = models.DateField(max_length=15, null=True)
    country = CountryField()
    user_type = models.CharField(max_length=10, choices=USERS, default="customer")

class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item_cost = models.DecimalField(max_digits=10, decimal_places=2)
