from django.db import models


#Import User
from django.contrib.auth.models import User
# Create your models here.



class Coffee(models.Model):
    brand = models.CharField(max_length=200)
    roast = models.CharField(max_length=200)
    flavor_profile = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)