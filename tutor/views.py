from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


# def index(request):
#     return HttpResponse("Ini Index")

# def recent(request):
#     return HttpResponse("Recent")

def about(request):
    return HttpResponse("Ini About")

def articles(request,year):
    year=year
    str = year
    return HttpResponse(year)