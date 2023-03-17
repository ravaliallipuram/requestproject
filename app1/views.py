from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    msg="<h1>This is view1</h1>"
    return HttpResponse(msg)
def view2(request):
    msg="<h1>This is view1</h1>"
    return HttpResponse(msg)
def home(request):
    h=render(request,"index.html")
    return h
