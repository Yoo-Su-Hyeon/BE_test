from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html')
    
def professor_list(request):
    professors = Professor.objects.all().order_by('-id')
    return render(request, 'professor_list.html', {'professors': professors})

def lecture_list(request):
    lectures = Lecture.objects.all().order_by('-id')
    return render(request, 'lecture_list.html', {'lectures': lectures})

def student_list(request):
    students = Student.objects.all().order_by('-id')
    return render(request, 'student_list.html', {'students': students})
