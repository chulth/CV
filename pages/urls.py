from django.urls import path
from django.views import index 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    ]