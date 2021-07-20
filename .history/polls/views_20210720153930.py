from django.http import HttpResponse

def index(request):
    return HttpResponse("Siemka :) Jesteś na stronie ")

def detail(request, question_id):
    return HttpResponse(f"Szukasz pytania {question_id}.")

def results(request, question_id):
    return HttpResponse(f"Szukasz odpowiedzi na pytanie {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"Głosujesz na pytanie {question_id}.")

