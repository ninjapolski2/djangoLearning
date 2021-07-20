from django.urls import path
from django.urls import views

urlPatterns = [path("", views.index, name="index"),]
