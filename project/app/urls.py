from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('',  views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('shop/',views.shop,name='shop'),
    path('checkout/',views.checkout,name='checkout'),
    path('cart/',views.cart,name='cart')
]