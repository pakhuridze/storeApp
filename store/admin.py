from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product


class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 30
    list_display = ('name', 'parent', 'created_at')


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "total_value", "description")
    readonly_fields = ("created_at", "updated_at")
    filter_horizontal = ("categories",)
    fields = (
        "name",
        "description",
        "price",
        "image",
        "quantity",
        "created_at",
        "updated_at",
        "categories",
    )



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
