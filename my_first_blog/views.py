from django.shortcuts import render
from django.http import HttpResponse
#from django.models import Blog
# Create your views here.
def lists(request):
    return render (request,'index.html')
def create(request):
     return HttpResponse("Hello Joyce")
def details(request):
    pass
def delete(request):
    pass