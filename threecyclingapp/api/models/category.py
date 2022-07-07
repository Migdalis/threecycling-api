#!/usr/bin/python3
"""
Holds Category Class
"""
from django.db import models
from .base_model import BaseModel


class Category(BaseModel, models.Model):
    """ Representation of a Category """
    name = models.CharField(unique=True, max_length=128)

    class Meta:
        db_table = 'categories'
