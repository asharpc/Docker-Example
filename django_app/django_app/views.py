from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>my docker</h1>")
   
def page(request):
    return HttpResponse("<h3>my docker</h3>")
   
