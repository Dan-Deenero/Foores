from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page(request):
    # Logic for customer dashboard
    return render(request, 'home.html')

@login_required(login_url='customer_login')
def customer_dashboard(request):
    # Logic for customer dashboard
    return render(request, 'customer/dashboard.html')

@login_required(login_url='restaurant_login')
def restaurant_dashboard(request):
    # Logic for restaurant owner dashboard
    return render(request, 'restaurant/dashboard.html')