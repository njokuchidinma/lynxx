from rest_framework import serializers
from .models import CustomUser, Category, Product, Order, OrderItem
from .country import CountryField



class CustomUserSerializer(serializers.ModelSerializer):
    country = CountryField()

    class Meta:
        model = CustomUser
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
