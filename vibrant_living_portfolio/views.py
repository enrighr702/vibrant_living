from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def coaching(request):
    return render(request, 'coaching.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', 'Not provided')
        message = request.POST.get('message')
        
        # Email content
        subject = f'New Contact Form Submission from {name}'
        email_message = f"""
        New contact form submission:
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        
        Message:
        {message}
        """
        
        try:
            # Send email
            send_mail(
                subject=subject,
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['ryanenright1202@gmail.com'],  # Your email
                fail_silently=False,
            )
            
            messages.success(request, 'Thanks for reaching out! I\'ll get back to you within 24 hours.')
            return redirect('index')  # Replace 'home' with your homepage URL name
            
        except Exception as e:
            messages.error(request, 'Something went wrong. Please email me directly at sean@vibrantliving.com')
            return redirect('home')
    
    return render(request, 'contact.html')

def testimonials(request):
    return render(request, 'testimonials.html')
