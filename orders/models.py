from django.db import models
from users.models import User
from products.models import Product

# ---------------------------
# Address Model
# ---------------------------
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    county = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.town}, {self.sub_county}, {self.county}"

# ---------------------------
# Order Model
# ---------------------------
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} - {self.status}"

# ---------------------------
# OrderItem Model
# ---------------------------
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        product_name = self.product.name if self.product else "Deleted Product"
        return f"{product_name} x {self.quantity}"

