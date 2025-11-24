from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class fraud_detection(models.Model):

    Order_ID= models.CharField(max_length=300)
    PDate= models.CharField(max_length=300)
    Status= models.CharField(max_length=300)
    Fulfilment= models.CharField(max_length=300)
    Sales_Channel= models.CharField(max_length=300)
    ship_service_level= models.CharField(max_length=300)
    Style= models.CharField(max_length=300)
    SKU= models.CharField(max_length=300)
    Category= models.CharField(max_length=300)
    PSize= models.CharField(max_length=300)
    ASIN= models.CharField(max_length=300)
    Qty= models.CharField(max_length=300)
    currency= models.CharField(max_length=300)
    Amount= models.CharField(max_length=300)
    payment_by= models.CharField(max_length=300)
    ship_city= models.CharField(max_length=300)
    ship_state= models.CharField(max_length=300)
    ship_postal_code= models.CharField(max_length=300)
    ship_country= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



