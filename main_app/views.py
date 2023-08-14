from django.shortcuts import render, redirect
from .models import Coffee
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
  return render(request, 'home.html')

def coffee_index(request):
  coffees = Coffee.objects.filter(user=request.user)
  return render(request, 'coffee/index.html', {
    'coffees': coffees
  })
  
def coffee_detail(request, coffee_id):
  coffee = Coffee.objects.get(id=coffee_id)
  return render(request, 'coffee/detail.html',{
    'coffee' : coffee
  })
  

def signup(request):
  error_message = ''
  if request.method == 'POST':
   
    form = UserCreationForm(request.POST)
    if form.is_valid():
      
      user = form.save()
      
      login(request, user)
      return redirect('/') # change back to index once we create the templae
    else:
      error_message = 'Invalid sign up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)