from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hai(request):
    return HttpResponse('this is our first fdv')
