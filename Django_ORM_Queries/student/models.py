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




