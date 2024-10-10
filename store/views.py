from django.http import JsonResponse
from .models import Product, Category


def category_view(request):
    categories = Category.objects.values()
    return JsonResponse({"categories": list(categories)})


def product_view(request):
    products = Product.objects.prefetch_related("categories").values(
        "id",
        "name",
        "description",
        "price",
        "image",
        "created_at",
        "updated_at",
    )

    product_list = []
    for product in products:
        category_names = Category.objects.filter(
            productcategory__product__id=product["id"]).values_list("name", flat=True)[::-1][0:1]

        product["categories"] = list(category_names)
        product_list.append(product)

    return JsonResponse({"products": product_list})
