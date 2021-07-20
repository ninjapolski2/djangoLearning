from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi, bro :) You are at the poll's index.")

def detail(request, question_id):
    return HttpResponse(f"Szukasz pytania {question_id}.")

def results(request, question_id):
    return HttpResponse(f"Szukasz odpowiedzi pytania {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"Głosujesz na pytanie ")

