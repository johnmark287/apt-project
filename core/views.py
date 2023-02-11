from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def index(request):
    return render(request, "core/index.html")

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(full_name = full_name, email =  email, subject = subject, message = message)
        messages.success (request, "your message was successfully recived")
        return redirect("index")

    #contact.save

    return render(request, "core/contact.html")

def about(request):
    return render(request, "core/about.html")

def dashboard(request):
    return render(request, "dashboard/index.html")
