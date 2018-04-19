from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=10000, blank=True)
    class Meta :
        verbose_name_plural = 'Categories'
        ordering = ['name']
    def __str__(self):
        return self.name
