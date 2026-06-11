from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.shortcuts import get_object_or_404
from .services.book_scraper import scrape_books
from .services.price_service import get_mock_price
from django.utils import timezone
from .models import PriceHistory


def product_list(request):
    products = Product.objects.all()

    context = {
        "products": products
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
            return redirect("product_list")

    else:
        form = ProductForm()

    return render(
        request,
        "add_product.html",
        {"form": form}
    )

def delete_product(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    product.delete()

    return redirect("product_list")

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

    product.current_price = get_mock_price()
    product.last_checked = timezone.now()

    product.save()

    PriceHistory.objects.create(
        product=product,
        price=product.current_price
    )

    return redirect(
        "product_list"
    )