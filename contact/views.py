from django.shortcuts import render

from .models import Contact


def contact(request):
    """
    A view to return the contact page, using the contact model here !!
    """
    print("test")

    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        contact = Contact(name=name, email=email, phone=phone, message=message)

        contact.save()

    return render(request, "contact/contact.html")
