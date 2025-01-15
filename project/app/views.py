from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def home(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'login.html')
def products_view(request):
    return render(request, 'products.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
            subject=f"New Contact: {subject}",
            message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')  

    return render(request, 'contact.html')

