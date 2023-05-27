from django.contrib import admin
from django.urls import path
from .views import  home, about, Login, signup, forgotPassword, contacts, shop, menu



urlpatterns = [
    path('home', home, name='home'),
    path('about/', about, name='about'),
    path('register/', signup, name='signup'),
    path('login/', Login, name='llogin'),
    path('forgotpass/', forgotPassword, name='forgotpass'),
    path('menu/', menu, name='menu'),
    path('shop/', shop, name='shop'),
    path('contacts/', contacts, name='contacts'),
]