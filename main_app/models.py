import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User



#Import User
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

RATING_CHOICES = [
    ('1', '1 - Poor'),
    ('2', '2 - Fair'),
    ('3', '3 - Good'),
    ('4', '4 - Very Good'),
    ('5', '5 - Excellent')
]




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
    

class User_review(models.Model):
    user_rating = models.CharField(
        choices = RATING_CHOICES,
        default = RATING_CHOICES[0][0]
    )
    user_review = models.TextField(max_length=250)
    
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_review
    def get_absolute_url(self):
        return reverse('detail', kwargs={'coffee_id': self.coffee.id})    


    
    # timestamp = models.DateTimeField(auto_now_add=True, null=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField ('date published') 
    def __str__(self):
        return self.question_text
    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Photo for coffee_id: {self.coffee_id} @{self.url}"

    