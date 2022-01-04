from rest_framework import serializers

from categories.serializers import CategorySerializer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'category',
            'price',
            'on_sale',
            'discount',
            'discounted_price'            
        ]