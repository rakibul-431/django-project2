from django.http import HttpResponse
from django.shortcuts import render

def contact(request):
    return HttpResponse("project file about section")
def home(request):
    return HttpResponse("this is home page")
def html(request):
    return render(request,'index.html')