from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    fb= models.CharField(max_length=100)
    desc= models.TextField()
    date= models.DateField()

    def __str__(self):
        return self.name


class Program(models.Model):
    head = models.CharField(max_length=15)
    strap = models.CharField(max_length= 30)
    desc = models.CharField(max_length=80)
    date= models.DateField()
    link = models.TextField()
    image = models.TextField()

    def __str__(self):
         return self.head + ' --> ' + self.strap
    
    
class Note(models.Model):
    head = models.CharField(max_length=15)
    strap = models.CharField(max_length= 30)
    desc = models.TextField()
    date= models.DateField()
    link = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.head + ' --> ' + self.strap
    
class Movie(models.Model):
    head = models.CharField(max_length=15)
    strap = models.CharField(max_length= 30)
    desc = models.TextField()
    date= models.DateField()
    link = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.head + ' --> ' + self.strap
    