from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list':}

def detail(request, question_id):
    return HttpResponse(f"Szukasz pytania {question_id}.")

def results(request, question_id):
    return HttpResponse(f"Szukasz wyników pytania {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"Głosujesz na pytanie {question_id}.")