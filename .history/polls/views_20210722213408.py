from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {'latest_question_list': latest_question_list,}
    return render(context, 'polls/index.html', request)

def results(request, question_id):
    return HttpResponse(f"Szukasz wyników pytania {question_id}.")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get 
    return HttpResponse(f"Głosujesz na pytanie {question_id}.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})