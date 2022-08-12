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


## Django ORM  inheritence options 

```
1. Abstract models 
2. Multi table model inheritence
3. Proxy model

```



