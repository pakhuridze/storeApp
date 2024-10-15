from django.core.paginator import Paginator
from django.db.models import Max, Min, Sum
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def category_view(request):
    categories = Category.objects.filter(parent=None).values('name')

    category_data = []
    for category in categories:
        subcategory_ids = list(Category.objects.filter(parent__name=category['name']).values_list('id', flat=True))
        parent_id = Category.objects.get(name=category['name']).id
        combined_ids = [parent_id] + subcategory_ids

        subcategories_product_count = Product.objects.filter(
            categories__id__in=combined_ids
        ).count()

        category_data.append({
            "name": category['name'],
            "id": parent_id,
            "subcategories_product_count": subcategories_product_count
        })

    return render(request, "category.html", {"categories": category_data})


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    categories = category.get_descendants(include_self=True)

    products = Product.objects.filter(categories__in=categories).distinct()
    most_expensive_product_price = products.aggregate(max_price=Max('price'))['max_price']
    most_lowest_product_price = products.aggregate(min_price=Min('price'))['min_price']
    sum_of_prices = products.aggregate(sum_of_prices=Sum('price'))['sum_of_prices']

    product_list = []
    for product in products:
        category_names = product.categories.values_list("name", flat=True)

        product_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "quantity": product.quantity,
            "categories": list(category_names),
            "total_value": product.total_value(),
        }
        product_list.append(product_data)

    # პაგინაცია: თითო გვერდზე 5 პროდუქტი
    paginator = Paginator(product_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,
                  "category_products.html",
                  {"page_obj": page_obj,
                   "category": category,
                   "most_expensive_product_price": most_expensive_product_price,
                   "most_lowest_product_price": most_lowest_product_price,
                   "sum_of_prices": sum_of_prices,
                   })


def product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    product_data = {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "quantity": product.quantity,
        "total_value": product.total_value(),
        "image": product.image.url if product.image and product.image != "" else None
    }

    product_list = [product_data]
    return render(request, "product_view.html", {"products": product_list})
