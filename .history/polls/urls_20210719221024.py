from django.urls import path
from django import views

urlPatterns = [path("", views.index, name="index"),]
