from django.contrib import admin
from .models import Coffee, User_review, Question


# Register your models here.
admin.site.register(Coffee)
admin.site.register(User_review)
admin.site.register(Question)

