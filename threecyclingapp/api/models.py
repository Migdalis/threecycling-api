# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)

    class Meta:
        db_table = 'categories'


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    categoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='categoryId')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    unitprice = models.IntegerField(db_column='unitPrice', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'products'


class Transactions(models.Model):
    id = models.IntegerField(primary_key=True)
    sellerid = models.ForeignKey('Users', models.DO_NOTHING, db_column='sellerId')  # Field name made lowercase.
    buyerid = models.ForeignKey('Users', models.DO_NOTHING, db_column='buyerId')  # Field name made lowercase.
    productid = models.ForeignKey(Products, models.DO_NOTHING, db_column='productId')  # Field name made lowercase.

    class Meta:
        db_table = 'transactions'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    department = models.CharField(max_length=128)
    city = models.CharField(max_length=128)

    class Meta:
        db_table = 'users'
