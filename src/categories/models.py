from django.db import models
from django.db.models.base import Model


class Category(models.Model):
    title = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categories'
        default_permissions = ()