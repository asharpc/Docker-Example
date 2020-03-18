from django.shortcuts import render

def home(request):
    return render(request, "<h1>my docker</h1>")
   
def page(request):
    return render(request, "<h3>...............first page.................</h3>")
   
