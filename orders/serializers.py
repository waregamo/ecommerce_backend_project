# orders/serializers.py
from rest_framework import serializers
from .models import Order, Address, OrderItem

# ----------------------
# Address Serializer
# ----------------------
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

# ----------------------
# Order Item Serializer
# ----------------------
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

# ----------------------
# Order Serializer
# ----------------------
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
