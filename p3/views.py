from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("<marquee>Hello ,Welcome To p3 Project</marquee>")
def home(request):
    return render(request,"simple.html")
def second(request):
    return render(request,"directory/second.html")
def third(request):
    return render(request,"directory/third.html",context={'data':"Akki",'name':"Akhil Chowdary Maguluri"})