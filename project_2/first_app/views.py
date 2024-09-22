from django.shortcuts import render

from django.http import HttpResponse

def about(request):
    return HttpResponse("I'm Rakibul islam. i complete creat to first app page")
def html3(request):
    return render(request,('first_app/home.html'))

# Create your views here.
