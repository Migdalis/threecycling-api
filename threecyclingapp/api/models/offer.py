#!/usr/bin/python3
"""
Holds Offer Class
"""
from django.db import models
from .base_model import BaseModel
from .user import User
from .product import Product


class Offer(BaseModel, models.Model):
    """ Representation of an Offer """
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, db_column='buyerId')  # Field name made lowercase.
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='productId')  # Field name made lowercase.
    status = models.CharField(max_length=15, blank=True, null=True)
    value = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        db_table = 'offers'
