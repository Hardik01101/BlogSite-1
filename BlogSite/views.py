from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signin(request):
    return render(request,'sign.html')