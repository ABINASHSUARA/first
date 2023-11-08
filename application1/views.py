from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jampandu(request):
    return HttpResponse("<h1><marquee>hiiii</marquee></h1>")

def jam(request):
    return HttpResponse("<h1><marquee>hello</marquee></h1>")
