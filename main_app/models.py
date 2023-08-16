import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User



#Import User
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

RATING_CHOICES = [(1,'1'),
                  (2,'2'),
                  (3,'3'),
                  (4,'4'),
                  (5,'5')]

RATING_CHOICES = [(1,'1'),
                  (2,'2'),
                  (3,'3'),
                  (4,'4'),
                  (5,'5')]



class User_review(models.Model):
    user_rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    user_review = models.TextField(max_length=250)

class Coffee(models.Model):
    brand = models.CharField(max_length=200)
    roast = models.CharField(max_length=200)
    flavor_profile = models.CharField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    review = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.brand} ({self.id})'
      
    def get_absolute_url(self):
        return reverse('detail', kwargs={'coffee_id': self.id})

    