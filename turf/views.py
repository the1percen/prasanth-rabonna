from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context=context)

def about(request):
    context = {}
    return render(request, "about.html", context=context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        if all([name, email, number, message]):
            contact = Contact(name=name, email=email, number=number, message=message)
            
            html = render_to_string("newcontact.html",{
                'name':name,
                'email':email,
                'number':number,
                'message':message,
            })
            send_mail('The contact form subject', 'This is the message', 'noreply@ulageshofficial.com', ['ulageshofficial@gmail.com'], html_message=html)
            contact.save()
            messages.success(request, "Thank you for contacting us. We will get back to you shortly.")
            return redirect('contact')  
        else:
            messages.error(request, "Please fill out all fields correctly.")

    return render(request, 'contact.html')

def booknow(request):
    image = Achievements.objects.all()
    context = {'image':image}
    return render(request, "booknow.html", context=context)
 
def achivements(request):
    context = {}
    return render(request, "achievements.html", context=context)