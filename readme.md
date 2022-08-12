## Manager in ORM

```
Manager is Django class which provides interface between database query operation and django model.

Application(Python) => ORM(Python to SQL) -> Adaptor/Driver => Database
```

## Queries
```

OR Queries

Get all data from table :- posts = Student.objects.all()  returns a queryset 

Filter with or considition(reuturns combine queryset) 
posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(
        surname__startswith='baldwin')

Q objects 
posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q(
        surname__startswith='baldwin') | Q(surname__startswith='avery-parker'))


And Queries

posts = Student.objects.filter(
        surname='austin') & Student.objects.filter(age__gt=19)
posts = Student.objects.filter(Q(surname='austin') & Q(age__gt=19))


Union Queries 

posts = Student.objects.all().values_list("firstname").union(
        Teacher.objects.all().values_list("firstname"))
<!-- values_list returns list of tuples but values returns list of objects(dict.) -->
<!-- Union removes  duplicates but union all does not -->

NOT Queries

posts= Student.objects.exclude(age=21)
posts=Student.objects.filter(~Q(age=21))


SELECT AND OUTPUT INDIVISUAL  FIELDS 

posts= Student.objects.filter(classroom=1).only('firstname','surname')

Simple Performing  Raw Queries 

posts = Student.objects.raw("SELECT  * from student_student")[:2]
print(posts)


SIMPLE BYPASS ORM 
 
cursor= connection.cursor()
cursor.execute("select count(*) from student_student")
r=cursor.fetchone()
print(r)


```


## Django ORM  inheritance options 

```
1. Abstract models 
2. Multi table model inheritance
3. Proxy model


Abstract model:- 

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

    
Multi table model inheritance:- allows one to one links 

class Books(models.Model):
    title=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)

class ISBN(Books):
    # books_ptr= models.OneToOneField(Books, on_delete=models.CASCADE,parent_link=True,primary_key=True)
    ISBN = models.TextField()

In ISBN table there will be two fields books_ptr_id(primary key foreign key to id column of books table) and ISBN     



PROXY MODELS :- 
change  the behavior of a model
proxy models operate  on the  original  model 
```

# Django ORM Query Optimization

```
django-debug-toolbar 

provide panel to show debug information 
System information 
timing 
setting/configurations 
header 
sql 
templates,includes 

```
## Aggregation in django 

```

class Book_agg(models.Model):

  title = models.CharField(_("title"), max_length=255)
  authors = models.CharField(_("authors"), max_length=255)
  average_rating = models.FloatField(_("average rating"))
  isbn = models.CharField(_("isbn"), max_length=150)
  isbn13 = models.CharField(_("isbn 13"), max_length=150)
  language_code = models.CharField(_("language code"), max_length=10)
  num_pages = models.IntegerField(_("number of pages"))
  ratings_count = models.BigIntegerField(_("rating count"))
  text_review_count = models.BigIntegerField(_("text review count"))
  publication_date = models.DateField(_("publication date"))
  publisher = models.CharField(_("publisher"), max_length=150)

def  book_agg(request):
    rating_count= Book_agg.objects.aggregate(Sum("ratings_count"))
    print(rating_count)

```

## Working with multiple databases 

```
create alias for one more database in django settings 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'users_db':{
         'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


```


## django  transaction atomicity 


```

from django.db import models

class customer(models.Model):
  name = models.CharField(max_length=50)
  balance = models.DecimalField(max_digits=5, decimal_places=2)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name




from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Payment
from .models import customer
from django.db.models import F
import decimal
from django.db import transaction

def process_payment(request):

  if request.method == 'POST':

    form = Payment(request.POST)

    if form.is_valid():
      x = form.cleaned_data['payor']
      y = form.cleaned_data['payee']
      z = decimal.Decimal(form.cleaned_data['amount'])

      payor = customer.objects.select_for_update().get(name=x)
      payee = customer.objects.select_for_update().get(name=y)

    with transaction.atomic():
      payor.balance -= z
      payor.save()

      payee.balance += z
      payee.save()

      # customer.objects.filter(name=x).update(balance=F('balance') - z)
      # customer.objects.filter(name=y).update(balance=F('balance') + z)

      return HttpResponseRedirect('/')

  else:
    form = Payment()

  return render(request, 'index.html', {'form': form})
```


## Foreign key constraint 

```
class Author(models.Model):
    name = models.CharField(max_length=512)
class Book(models.Model):
    title = models.CharField(max_length=512)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

To define a relationship between two models, you need to define the ForeignKey field in the model from the Many side of the relationship.  In other words, ForeignKey should be placed in the Child table, referencing the Parent table.

NOTE - Without an Author, there can't be Book (Author is parent, Book is child model)
```

## Django Signals 

```
from django.db.models.signals import pre_delete, post_delete
from .models import Student
from django.dispatch import receiver

@receiver(pre_delete, sender=Student)
def pre_delete_profile(sender, **kwargs):
    print("You are about to delete something!")

@receiver(post_delete, sender=Student)
def delete_profile(sender, **kwargs):
    print("You have just deleted a student!!!")
```