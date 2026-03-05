from rest_framework import serializers
from .models import Cart,CartItem,Order,OrderItem
from products.models import Product
from products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only = True)
    product_id = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all(),source = "product",write_only = True)

    subtotal = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = ["id", "product", "product_id", "quantity", "subtotal"]

class CartSerializer(serializers.ModelSerializer):

    items = CartItemSerializer(read_only = True,many =True)
    total = serializers.ReadOnlyField()

    class Meta:
         model = Cart
         fields = ["id", "items", "total"]

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    subtotal = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price", "subtotal"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id", "status", "payment_status", "stripe_session_id",
            "total_price", "shipping_address", "items", "created_at"
        ]
        read_only_fields = ["id", "status", "payment_status", "stripe_session_id", "total_price", "created_at"]


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["shipping_address"]
        extra_kwargs = {
            "shipping_address": {"required": False}
         }