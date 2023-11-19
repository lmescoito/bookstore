from rest_framework import serializers

from product.models.product import Product
from product.serializers.category_serialize import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    categoru = CategorySerializer(required=True, many=True)

    class Meta:
        model: Product
        fields = ['title', 'description', 'price', 'active', 'category']
