from rest_framework import serializers

from product.serializers import ProductSerializer
from product.models import Product
from order.models import Order

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instace):
        total = sum([product.price for product in instace.product.all()])
        return total

    class Meta:
        model = Order
        field = ['product', 'total', 'user', 'products_id'],
        extra_kwargs = {'product': {'required': False}}
    
    def created(self, validated_data):
        product_data = validated_data.pop('product_id')
        user_data = validated_data.pop('user')

        order = Order.objects.create(user=user_data)
        for product in product_data:
            order.product.add(product)
        
        return order