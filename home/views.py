from django.shortcuts import render
from datetime import date, datetime
from home.models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        fb= request.POST.get('fb')
        desc= request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, fb=fb, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')

