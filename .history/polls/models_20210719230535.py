from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.CharField
# Create your models here.
