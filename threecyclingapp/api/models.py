from django.db import models


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


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)

    class Meta:
        db_table = 'categories'


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    categoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='categoryId')  # Field name made lowercase.
    userid = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='userId')  # Field name made lowercase.
    unitprice = models.IntegerField(db_column='unitPrice', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'products'


class Offers(models.Model):
    id = models.IntegerField(primary_key=True)
    buyerid = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='buyerId')  # Field name made lowercase.
    productid = models.ForeignKey(Products, on_delete=models.CASCADE, db_column='productId')  # Field name made lowercase.
    status = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'offers'
