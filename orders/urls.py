# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Orders
    path("", views.OrderListView.as_view(), name="order-list"),
    path("<int:pk>/", views.OrderDetailView.as_view(), name="order-detail"),

    # Addresses
    path("addresses/", views.AddressListView.as_view(), name="address-list"),
    path("addresses/<int:pk>/", views.AddressDetailView.as_view(), name="address-detail"),

    # Order Items
    path("items/", views.OrderItemListView.as_view(), name="orderitem-list"),
    path("items/<int:pk>/", views.OrderItemDetailView.as_view(), name="orderitem-detail"),
]
