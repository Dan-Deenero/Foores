from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm

# Create your views here.
@login_required
def home(request):
    if request.user.is_authenticated:
        #we are passing in the data from the category model
        return render(request, "customer/index.html",)
    else:
        return redirect("login")
@login_required
def about(request):
    if request.user.is_authenticated:
        return render(request, "customer/about.html")
    else:
        return redirect("login")
@login_required
def menu(request):
    if request.user.is_authenticated:
        #we are passing in the data from the category model
        return render(request, "customer/menu.html",)
    else:
        return redirect("login")
    
@login_required
def shop(request):
    if request.user.is_authenticated:
        #we are passing in the data from the category model
        return render(request, "customer/shop.html",)
    else:
        return redirect("login")
    
@login_required
def contacts(request):
    if request.user.is_authenticated:
        #we are passing in the data from the category model
        return render(request, "customer/contacts.html",)
    else:
        return redirect("login")
    
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password') 
            user = authenticate(username=username, password=password) 
            login(request, user) 
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'customer/signup.html', {
        'form': form
    })

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is Incorrect!!!")
    return render(request, 'customer/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def forgotPassword(request):
    return render(request, 'customer/forgot-password.html')