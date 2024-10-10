from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product, ProductCategory


class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 30
    list_display = ('name', 'parent', 'created_at')

class ProductAdminInline(admin.StackedInline):
    model = ProductCategory
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")
    readonly_fields = ("created_at", "updated_at")
    inlines = [ProductAdminInline]
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
