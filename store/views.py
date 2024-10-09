from django.http import JsonResponse
from .models import Product, ProductCategory, Category


def category_view(request):

    categories = Category.objects.values()
    return JsonResponse({"categories": list(categories)})


def product_view(request):

    products = Product.objects.values()
    for product in products:
        product["categories"] = list(
            ProductCategory.objects.filter(product_id=product["id"]).values_list(
                "category__name"
            )[::-1][0:1]
        )
    return JsonResponse({"products": list(products)})