#!/usr/bin/python3
"""
Holds User Class
"""
from django.db import models
from .base_model import BaseModel


class User(BaseModel, models.Model):
    """ Representation of an User """
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    department = models.CharField(max_length=128)
    city = models.CharField(max_length=128)

    class Meta:
        db_table = 'users'
