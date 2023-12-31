from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coffee/', views.coffee_index, name='index'),
    path('coffee/<int:coffee_id>/', views.coffee_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('coffee/create/', views.CoffeeCreate.as_view(), name='coffee_create'),
    path('coffee/<int:pk>/update/', views.CoffeeUpdate.as_view(), name='coffee_update'),
    path('coffee/<int:pk>/delete/', views.CoffeeDelete.as_view(), name='coffee_delete'),
    path('coffee/<int:coffee_id>/add_review/', views.add_review, name='add_review'),
    path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='reviews_update'),
    path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='reviews_delete'),
    path('coffee/<int:coffee_id>/add_photo/', views.add_photo, name='add_photo'),
    path('search/', views.search_coffee, name='coffee_search'),
]