from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

# Create your models here.
#auth table
class Auth(models.Model):
    userid = models.CharField("id",max_length=40)
    pasword = models.CharField("pasword",max_length=40)
    
#customer 1 table    
class Customer1(models.Model):
    orderDate = models.DateField()
    company = models.CharField(max_length=50, validators=[alphanumeric])
    owner = models.CharField(max_length=50, validators=[alphanumeric])
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    weight = models.FloatField()
    shipment = models.CharField(max_length=255)
    trackingId=models.CharField(max_length=255)
    shipmentSize = models.CharField(max_length=20)
    boxCount =models.IntegerField()
    specification = models.CharField(max_length=255)
    checklistQuantity = models.CharField(max_length=255)
    
#customer 2 table    
class Customer2(models.Model):
    orderDate = models.DateField()
    company = models.CharField(max_length=50, validators=[alphanumeric])
    owner = models.CharField(max_length=50, validators=[alphanumeric])
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    weight = models.FloatField()
    shipment = models.CharField(max_length=255)
    trackingId=models.CharField(max_length=255)
    shipmentSize = models.CharField(max_length=20)
    boxCount =models.IntegerField()
    specification = models.CharField(max_length=255)
    checklistQuantity = models.CharField(max_length=255)