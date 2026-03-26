from django.urls import path
from .views import *

app_name = 'welcome_app'

urlpatterns = [
    path('', index, name='index'),
    path('welcome/', welcome, name='welcome'),
]
