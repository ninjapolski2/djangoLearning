from django.urls import path
from django.urls.contrib.auth import views

urlPatterns = [path("", views.index, name="index"),]
