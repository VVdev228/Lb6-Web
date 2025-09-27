from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#views
def index(request):
    return HttpResponse('Shop 2 is working')
