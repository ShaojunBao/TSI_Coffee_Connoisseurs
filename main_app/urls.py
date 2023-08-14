from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coffee/', views.coffee_index, name='index'),
    path('coffee/<int:coffee_id>/', views.coffee_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
]