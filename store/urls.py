from django.urls import path
from .views import category_view, product_view
urlpatterns = [
    path('category/', category_view, name="category")
    ,path('product/', product_view, name="product")
]