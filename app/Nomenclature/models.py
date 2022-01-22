from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CODE = [
        ('in_stock', 'In stock'),
        ('out_of_stock', 'Out of stock')
    ]

    name = models.CharField(max_length=8, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CODE)
    remains = models.PositiveIntegerField()

    def __str__(self):
        return self.name
