from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#this post model is a class that inherits from django model class
#
class Post(models.Model): #inherits from model.model each class will be own table in database
    title=models.CharField(max_length=100) #each field is an attribute of the class
    content=models.TextField() #
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete is a function that deletes posts when user is deleted


def __str__(self):
    return self.title
   
 #migrate command creates database manage.py migrate 
 #migrations makes it possible to make changes to databse without writing pure SQL 
 #user model is a seperate database
#one to many relationship is created by using models.ForeignKey
#manage.py sqlmigrate 001 in cmd displays raw sql code
