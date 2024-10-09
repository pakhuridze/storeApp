from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product, ProductCategory


class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 30

class ProductCategoryInline(admin.StackedInline):
    model = ProductCategory
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at", "description")
    inlines = [ProductCategoryInline]
    readonly_fields = ("created_at", "updated_at")
    fields = (
        "name",
        "description",
        "price",
        "image",
        "created_at",
        "updated_at",
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)