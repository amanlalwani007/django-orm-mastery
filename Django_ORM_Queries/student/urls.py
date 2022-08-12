from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list_bypass_orm, name='student_data'),
]
