from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=150, verbose_name="სახელი")
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="მშობელი კატეგორია",
        related_name="children",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="დასახელება")
    description = models.TextField(verbose_name="აღწერა")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ფასი")
    image = models.ImageField(upload_to="products/", verbose_name="სურათი", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, verbose_name="კატეგორიები", related_name="products")
    quantity = models.PositiveIntegerField(default=0, verbose_name="რაოდენობა")

    def __str__(self):
        return self.name

    def total_value(self):
        return round(self.price * self.quantity,0)

