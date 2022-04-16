from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def philosophy(request):
    return render(request, "philosophy.html")    

def calculate(request):
    return render(request, "calculator.html")
