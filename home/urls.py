from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("home", views.index, name='home'),
    path("contact", views.contact, name='rate Us'),
    path("code", views.code, name='code'),
    path("note", views.note, name='note'),
    path("movie", views.movie, name='movie'),
]
