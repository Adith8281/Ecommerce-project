from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('login/', views.login_view, name='login'), 
    path('products/', views.products_view, name='products'), 
    path('contact/', views.contact_view, name='contact'),
]


