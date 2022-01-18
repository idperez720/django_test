from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def addPoll(request):
    return HttpResponse('Create new poll')