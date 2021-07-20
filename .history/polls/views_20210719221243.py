from django.http import HttpResponse

async def index(request):
    return HttpResponse("Hi, bro :) You are at the poll's index.")


# Create your views here.
