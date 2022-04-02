from asyncio.windows_events import NULL
from distutils.archive_util import make_zipfile
from distutils.command.upload import upload
from email.mime import image
from pyexpat import model
from tkinter import CASCADE, image_names
from unicodedata import name
from django.db import models
from flask import request


# Create your models here.          
# 
# For Many to Many relationship                
class Tag(models.Model): 
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"

# one to Many 
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    profile_picture = models.CharField(max_length=10, null=True)
    short_intro = models.CharField(max_length=200, null=True)
    job_title = models.CharField(max_length=50, null= True)


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()



class Post(models.Model):
    title = models.CharField(max_length=100)
    description  = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", max_length=50, null=True, blank=True, default="images/default.jpg")
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    slug =models.SlugField(unique=True, db_index=True)
    author =models.ForeignKey(Author, on_delete= models.SET_NULL, null=True, related_name="post")

    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return f"{self.title} {self.author}"


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name= "comment")

class Contact(models.Model):
    title = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    message = models.TextField()


