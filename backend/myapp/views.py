from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect



def index(request): 
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contact=Contact()
        contact.name=name
        contact.email=email
        contact.phone=phone
        contact.message=message
        contact.save()
        print("## Data has been written to the database")
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('index')
        # return HttpResponse("<h1>Successful</h1>")
    # messages.info(request, 'Welcome to our website!')
    return render(request, "index.html")

def pitchdeck(request):
    return render(request, "pitchdeck.html")
