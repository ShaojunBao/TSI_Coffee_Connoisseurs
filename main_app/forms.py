from django.forms import ModelForm
from .models import User_review

class CommentForm(ModelForm):
  class Meta:
    model = User_review
    fields = ['user_rating', 'user_review']
    