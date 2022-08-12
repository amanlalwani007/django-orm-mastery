from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################


def student_list_(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


def student_list_(request):
    posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(
        surname__startswith='baldwin')

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


def student_list__(request):
    posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q(
        surname__startswith='baldwin') | Q(surname__startswith='avery-parker'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


# And  Queries


def student_list__and(request):
    # posts = Student.objects.filter(
    #     surname='austin') & Student.objects.filter(age__gt=19)
    posts = Student.objects.filter(Q(surname='austin') & Q(age__gt=19))
    print(posts)
    print(connection.queries)
    return render(request, 'output.html', {'posts': posts})


# union queries


def student_list__union(request):
    posts = Student.objects.all().values_list("firstname").union(
        Teacher.objects.all().values_list("firstname"))
    print(posts)
    print(connection.queries)
    # value_list returns list of tuples but value returns  dictionary 
    
    return render(request, 'output.html', {'posts': posts})


#not queries

def student_list__not(request):
    # posts= Student.objects.exclude(age=21)
    posts=Student.objects.filter(~Q(age=21))
    print(posts)
    print(connection.queries)
    return render(request,'output.html', {'posts':posts}) 


    

# Select and output  indivisual fields  

def student_list__selectindv(request):
    posts= Student.objects.filter(classroom=1).only('firstname','surname')
    print(posts)
    print(connection.queries)
    return render(request,'output.html', {'posts':posts}) 


# RAW QUERIES 


def  student_list_raw_query(request):
    # posts=Student.objects.all()
    posts = Student.objects.raw("SELECT  * from student_student")[:2]
    print(posts)
    print(connection.queries)
    return render(request,'output.html', {'posts':posts})


# SIMPLE BYPASS ORM

def student_list_bypass_orm(request):
    cursor= connection.cursor()
    cursor.execute("select count(*) from student_student")
    r=cursor.fetchone()
    print(r)


