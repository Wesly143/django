from django.shortcuts import render
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages
from home.models import Program
from home.models import Note

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
    alpost = Program.objects.all()
    context = {'alpost': alpost}
    return render(request, 'code.html', context)


def note(request):
    allnotes = Note.objects.all()
    context = {'allnotes': allnotes}
    return render(request, 'note.html', context)

def movie(request):
    return render(request, 'movie.html')