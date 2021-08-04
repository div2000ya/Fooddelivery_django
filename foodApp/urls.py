from foodApp.models import Restaurant
from django import urls
from django.urls import path
from foodApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("register/", views.register_request, name="Register"),
    path("login/", views.login_request, name="Login"),
    path('', views.home, name="Home"),
    path('restaurants/', views.FoodRestaurant, name="Restaurant"),
    path('menu/',views.menu, name="Menu"),
    path('cart/<int:pk>',views.Order.as_view(), name="Cart"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)