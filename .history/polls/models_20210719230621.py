from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Data opublikowania')
# Create your models here.

class Choice(models.Model):
    question = 
