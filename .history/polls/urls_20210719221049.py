from django.urls import path
from django.contrib.auth import views

urlPatterns = [path("", views.index, name="index"),]
