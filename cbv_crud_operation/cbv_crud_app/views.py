from django.shortcuts import render
from .forms import TeamDetail
from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello')
