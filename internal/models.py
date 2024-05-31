from django.db import models
from django.db.models.base import Model

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name

class ProgrammingLanguage(models.Model):
    name=models.CharField(max_length=15)
    title=models.CharField(max_length=60)
    description = models.TextField()
    img = models.ImageField(upload_to="Langauge")
    
    def __str__(self):
        return self.name

class Blogs(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title

class Internship(models.Model):
    fullname=models.CharField(max_length=60)
    usn=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    college_name=models.CharField(max_length=100)
    course=models.CharField(max_length=60)
    programming_langauge=models.CharField(max_length=60)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.usn


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="About service")

    def __str__(self):
        return self.name

