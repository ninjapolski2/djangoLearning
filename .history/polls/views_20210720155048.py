from django.http import HttpResponse
from .models import 

def index(request):
    latest_question_list = Question.objects.get

