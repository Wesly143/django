from django.shortcuts import render
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages
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
        messages.success(request, 'Sent Successfully!!')
    return render(request, 'contact.html')


def code(request):
    return render(request, 'code.html')


def note(request):
    return render(request, 'note.html')

def movie(request):
    return render(request, 'movie.html')