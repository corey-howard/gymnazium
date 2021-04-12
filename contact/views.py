from django.shortcuts import render
from django.contrib import messages
from .models import Contact


def contact(request):
    """
    A view to return the contact page, using the contact model here !!
    """
    print("test")

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone, message=message)

        contact.save()

        messages.success(request, 'Thank you for your message, we will get back to you as soon as possible.')

    return render(request, "contact/contact.html")
