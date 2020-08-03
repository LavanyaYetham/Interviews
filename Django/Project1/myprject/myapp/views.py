from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello World</h1>")
def index(request):
    now=datetime.datetime.now()
    html="<html><body><h3>Now time is %s </h3></body></html>"%now
    return HttpResponse(html)

