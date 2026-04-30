from django.urls import path
from .views import *

app_name = 'lectures'

urlpatterns = [
    path('', index, name='index'),
    path('professor_list/', professor_list, name ='professor_list'),
    path('lecture_list/', lecture_list, name='lecture_list'),
    path('student_list/', student_list, name='student_list'),

]
