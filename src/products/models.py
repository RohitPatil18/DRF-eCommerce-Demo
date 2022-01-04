from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

from categories.models import Category


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.PositiveIntegerField(
        default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    on_sale = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        default_permissions = ()

    @property
    def discounted_price(self) -> float:
        if self.on_sale:
            return round(self.price * self.discount / 100, 2)

