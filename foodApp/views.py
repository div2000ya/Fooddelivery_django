from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .form import NewUserForm
from django.http import HttpResponse
from django.views import View
# Create your views here.

# def logout_request(request):
#     logout(request)
#     HttpResponse(request,'logout')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="signup.html", context={"register_form":form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}")
                return redirect('Restaurant')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})




def FoodRestaurant(request):
    data = Restaurant.objects.all()
    return render (request, 'main.html', {'data':data})

def home(request):
    return render(request,'index.html')

def menu(request):
    restaurant_Id = request.GET.get("id")
    data =Fooditem.objects.filter(restaurant=restaurant_Id)
    return render(request,'menu.html',{'data':data})

class Order(View):
    def get(self,request,pk = None):
        if request.method =="GET": 
            fooditem = Fooditem.objects.filter(id = pk)
            print(fooditem)
            data = {
                "fooditem":fooditem,
                }
            return render(request,'cart.html',data)

    def post(self,request,pk=None):
        
        postdata = request.POST
        f_name = postdata.get('f_name')
        f_price = postdata.get('f_price')
        phoneno = postdata.get('phoneno')
        address = postdata.get('address')
        print(f_name,f_price,phoneno,address)
        order = Cart(
                        f_name=f_name,
                        f_price=f_price,
                        phoneno=phoneno,
                        address=address,
                    )
        order.save()
        message = "Thankyou for Order Your Oder is Successfully Taken"
        data = {
                "message":message
        }
        return render(request,'cart.html',data)

    