"""
This is the file mostly related to database.
"""
import datetime
from django.db import models


class Category(models.Model):
    """
    This class is for category.
    """
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        """This is meta class for category name change."""
        verbose_name_plural = 'categories'


class Customer(models.Model):
    """
    This class is for customer details.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    """
    This class is for product details.
    """
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    # add sale stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    def __str__(self) -> str:
        return f'{self.name}'


class Order(models.Model):
    """
    This is the order class where all the order details will store.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=13, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.product}"
    