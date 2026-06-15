from django.urls import path
from . import views
urlpatterns = [
    path("products/", views.product_list, name="product_list"),
    path("add-product/", views.add_product, name="add_product"),
    path(
        "delete-product/<int:product_id>/",
        views.delete_product,
        name="delete_product"
    ),
    path(
    "edit-product/<int:product_id>/",
    views.edit_product,
    name="edit_product"),

    path(
    "scrape-books/",
    views.scrape_books_view,
    name="scrape_books"),

    path(
    "update-price/<int:product_id>/",
    views.update_price,
    name="update_price"),

    path(
    "price-history/<int:product_id>/",
    views.price_history,
    name="price_history"),

    path(
    "update-all-prices/",
    views.update_all_prices,
    name="update_all_prices"),
]