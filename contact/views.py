from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


# Create your views here.

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST ['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)

        contact.save()

        # Send email
        send_mail(
            'Foodie Jerry Inquiry',
            'There has been Inquiry for ' + name + '. Sign into the admin panel for more',
            'jerry.jagtap5@gmail.com',
            ['nishjagtap5596@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been sent, a realtor will get back to you soon')

        return redirect('/')


