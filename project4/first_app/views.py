from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("That is prom first_app ...we can creat first app sucessfully")
def first_app_home(request):
    return HttpResponse("This is first app Home page")
