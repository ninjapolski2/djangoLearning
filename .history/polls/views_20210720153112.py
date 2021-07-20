from django.http import HttpResponse

async def index(request):
    return HttpResponse("Hi, bro :) You are at the poll's index.")

async def detail(request, question_id):
    response = ""