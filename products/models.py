from django.db import models

# ---------------------------
# Category
# ---------------------------
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ---------------------------
# Product
# ---------------------------
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

# ---------------------------
# ProductImage
# ---------------------------
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField()
    is_main = models.BooleanField(default=False)  # optional: marks main image

    def __str__(self):
        return f"{self.product.name} Image"
