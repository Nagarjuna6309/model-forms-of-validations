from django.urls import path
from app.views import *
app_name='naga'

urlpatterns = [
    path('brock/',brock,name='brock'),
]
