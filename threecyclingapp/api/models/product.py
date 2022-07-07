"""
Holds Product Class
"""
from django.db import models
from .base_model import BaseModel
from .category import Category
from .user import User


class Product(BaseModel, models.Model):
    """ Representation of a Product """
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='categoryId')  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='userId')  # Field name made lowercase.
    price = models.IntegerField(db_column='unitPrice', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=15, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'products'
