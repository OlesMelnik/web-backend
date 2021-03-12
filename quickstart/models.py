from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    product_type = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Category(models.Model):
    name = models.CharField(max_length=30)
    category_type = models.CharField(max_length=30)
    description = models.CharField(max_length=30)