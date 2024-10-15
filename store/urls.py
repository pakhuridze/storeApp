from django.urls import path
from .views import category_view, product_view, category_products
urlpatterns = [
    path('category/', category_view, name="category_view")
    ,path('product/<int:product_id>/', product_view, name="product_view"),
    path('category/<int:category_id>/products/', category_products, name='category_products'),

]
