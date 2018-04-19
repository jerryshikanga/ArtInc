from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone

# Create your models here.
class Bid(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    amount = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    success = models.BooleanField(default=False)
