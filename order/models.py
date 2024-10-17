from django.db import models
from django.conf import settings


class OrderItem(models.Model):
    cart = models.ForeignKey('UserCart', on_delete=models.CASCADE)
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart}"


class UserCart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('store.Product', through='OrderItem')

    def __str__(self):
        return f"Cart for {self.user.email}"