from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


def contact(request):
    """
    A view to return the contact page
    """

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone, message=message)

        contact.save()

        # Send email
        send_mail(
            'You have been sent a message via Gone Fishing.',
            'The message was sent from ' + name
            + '. View this message in the admin.',
            'EMAIL_HOST_USER',
            ['sales@gymnazium.co.uk', 'coreyhoward@live.co.uk'],
            fail_silently=False
        )

        messages.success(request, 'Thank you for your message, we will get back to you as soon as possible.')

    return render(request, "contact/contact.html")
