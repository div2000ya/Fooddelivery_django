from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
# Create your models here.
def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})

class Restaurant(models.Model):
    r_name = models.CharField(max_length=100)
    r_contact = models.CharField(max_length=100)
    
    def __str__(self):
        return self.r_name

class Fooditem(models.Model):
    f_name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    f_price = models.IntegerField()
    f_image = models.ImageField(upload_to = 'media')

    def __str__(self):
        return self.f_name

class Cart(models.Model):
    f_name = models.CharField(max_length=100)
    f_price = models.IntegerField()
    phoneno = models.CharField(max_length=100, default=None)
    address = models.CharField(max_length=100, default=None)
    
    def __str__(self):
        return self.f_name