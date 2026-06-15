from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.utils import timezone
from django.db import models

from .models import (
    Product,
    PriceHistory
)

from .forms import ProductForm

from .services.book_scraper import (
    scrape_books,
    get_book_price
)


def product_list(request):

    products = Product.objects.all()

    total_products = products.count()

    ready_to_buy = products.filter(
        current_price__lte=models.F("target_price")
    ).count()

    average_price = 0

    if total_products > 0:

        average_price = (
            sum(
                product.current_price
                for product in products
            ) / total_products
        )

    context = {
        "products": products,
        "total_products": total_products,
        "ready_to_buy": ready_to_buy,
        "average_price": average_price
    }

    return render(
        request,
        "products.html",
        context
    )


def add_product(request):

    if request.method == "POST":

        form = ProductForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                "product_list"
            )

    else:

        form = ProductForm()

    return render(
        request,
        "add_product.html",
        {
            "form": form
        }
    )


def edit_product(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            instance=product
        )

        if form.is_valid():

            form.save()

            return redirect(
                "product_list"
            )

    else:

        form = ProductForm(
            instance=product
        )

    return render(
        request,
        "edit_product.html",
        {
            "form": form
        }
    )


def delete_product(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    product.delete()

    return redirect(
        "product_list"
    )


def scrape_books_view(request):

    books = scrape_books()

    return render(
        request,
        "scraped_books.html",
        {
            "books": books
        }
    )


def update_price(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    product.current_price = get_book_price(
        product.url
    )

    product.last_checked = timezone.now()

    product.save()

    PriceHistory.objects.create(
        product=product,
        price=product.current_price
    )

    return redirect(
        "product_list"
    )


def update_all_prices(request):

    products = Product.objects.all()

    for product in products:

        try:

            product.current_price = get_book_price(
                product.url
            )

            product.last_checked = timezone.now()

            product.save()

            PriceHistory.objects.create(
                product=product,
                price=product.current_price
            )

        except Exception as e:

            print(
                f"Error updating {product.name}: {e}"
            )

    return redirect(
        "product_list"
    )


def price_history(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    history = product.price_history.all().order_by(
        "-checked_at"
    )

    return render(
        request,
        "price_history.html",
        {
            "product": product,
            "history": history
        }
    )