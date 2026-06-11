from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)

    url = models.URLField()

    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    target_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    last_checked = models.DateTimeField(
    null=True,
    blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
    


class PriceHistory(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="price_history"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    checked_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.product.name} - {self.price}"