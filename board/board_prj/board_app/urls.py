from django.urls import path
from .views import *

app_name = 'board_app'

urlpatterns=[
    path('', index, name='index'),
]