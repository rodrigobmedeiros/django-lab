from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def home_page_view(request: HttpRequest):
    return HttpResponse("Hello, world!")
