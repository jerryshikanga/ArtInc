from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from categories.models import Category
from django.db.models import Max, Avg, Count, Min

class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate( Min('bid__amount'), Max('bid__amount'), Count('bid'), Avg('bid__amount'))

# Create your models here.

class Product(models.Model):
    """docstring for Product."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=20)
    description = models.CharField(max_length=10000, blank=True)
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="uploads/product/photo/", blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.name

    def is_active(self):
        return self.active

    def get_queryset(self):
        return super().get_queryset().annotate(Count('bid'), Max('bid'), Avg('bid'))
