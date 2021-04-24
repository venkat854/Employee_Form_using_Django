from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from .models import Contact

def index(request):
    if request.method=="POST":
        id = request.POST.get('id','')
        name = request.POST.get('name','')
        city = request.POST.get('city','')
        contact = request.POST.get('contact','')
        email = request.POST.get('email','')
        if id and name and city and contact and email:
            contact = Contact(id=id,name=name,city=city,contact=contact,email=email)
            contact.save()
        else:
            return HttpResponse("enter all the details")
    return render(request, "index.html")

# Create your views here.
