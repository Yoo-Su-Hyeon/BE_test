from django.contrib import admin
from .models import *

admin.site.register(Professor)
admin.site.register(Lecture)
admin.site.register(Student)
admin.site.register(LectureStudent)


