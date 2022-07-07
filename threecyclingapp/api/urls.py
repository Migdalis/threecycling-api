from django.urls import path
from .views.products import *


urlpatterns = [
    path("products", get_products, name="get_products"),
    path("product/<int:product_id>/", get_product, name="get_product"),
    path("product-category/<int:category_id>/", get_product_category, name="get_product_category"),
    path("product-category/<str:category_name>/", get_product_category_name, name="get_product_category_name"),
    path("product-user/<int:user_id>/", get_product_user, name="get_product_user")
]
