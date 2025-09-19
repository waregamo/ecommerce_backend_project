from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order, Address, OrderItem
from .serializers import OrderSerializer, AddressSerializer, OrderItemSerializer

# ----------------------
# Orders
# ----------------------
class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "user"]
    search_fields = ["user__username", "address__town"]
    ordering_fields = ["created_at", "status"]

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# ----------------------
# Addresses
# ----------------------
class AddressListView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


# ----------------------
# Order Items
# ----------------------
class OrderItemListView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer