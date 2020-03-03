from django.db import models


# Create your models here.
# Product class inherits models.Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    img_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    discount = models.FloatField()
