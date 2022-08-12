from distutils.command.upload import upload
from time import timezone
from typing import OrderedDict
from django.db import models

# Model Tasks 1-5
#####################################

class Teacher(models.Model):
      
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class Student(models.Model):
      
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

######################################

#Abstract model 

class BaseItem(models.Model):
    title=models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True
        ordering = ['title']

class ItemA(BaseItem):
    content= models.TextField()
    class Meta(BaseItem.Meta):
        ordering=['-created']

class ItemB(BaseItem):
    file=models.FileField(upload_to='files')

class  ItemC(BaseItem):
    file=models.FileField(upload_to='images')

class ItemD(BaseItem):
    slug=models.SlugField(max_length=255,unique=True)  






# Multi table model inheritance
class Books(models.Model):
    title=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)

class ISBN(Books):
    # books_ptr= models.OneToOneField(Books, on_delete=models.CASCADE,parent_link=True
    # ,primary_key=True)
    ISBN = models.TextField()



# Proxy model 
class BookContent(models.Model):
    title=models.CharField(max_length=100)
    created= models.DateTimeField(auto_now_add=True)


class BookOrders(BookContent):
    class Meta:
        proxy=True
        ordering=['created']
    def created_on(self):
        return timezone.now()-self.created    





class Book_agg(models.Model):

  title = models.CharField(max_length=255)
  authors = models.CharField(max_length=255)
  average_rating = models.FloatField()
  isbn = models.CharField(max_length=150)
  isbn13 = models.CharField(max_length=150)
  language_code = models.CharField(max_length=10)
  num_pages = models.IntegerField()
  ratings_count = models.BigIntegerField()
  text_review_count = models.BigIntegerField()
  publication_date = models.DateField()
  publisher = models.CharField(max_length=250)