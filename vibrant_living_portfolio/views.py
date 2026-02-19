from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def coaching(request):
    return render(request, 'coaching.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', 'Not provided').strip()
        message = request.POST.get('message', '').strip()
        
        # Basic validation (no email needed!)
        if name and email and message:
            messages.success(request, 
                f'Thanks {name}! Your info is saved. Check your inbox for confirmation.')
        else:
            messages.error(request, 'Please fill name, email, and message.')
        
        # Redirect to homepage (your Apps Script handles Sheet saving)
        return redirect('index')  # or 'home'
    
    return render(request, 'contact.html')


def testimonials(request):
    return render(request, 'testimonials.html')
