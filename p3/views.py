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
def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange']
    return render(request,"directory/fourth.html",{'fruits':fruits})
def fifth(request):
    return render(request,"directory/fifth.html",{'a':10,'b':17})
def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))
def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))
def ac(request,c,d):
    if  int (c) > int (d):
        greatest = " c Value  is Greatest", c
    elif int(d) > int(c):
        greatest = " d Value  is Greatest", d
    else:
        greatest = " Two Values are equal numbers",c,d
    context = {"greatest":greatest}
    return render(request,"directory/greatest.html",context)
def ad(request,e,f,g):
    if  int (e) > int (f) and int (e) > int (g):
        greatest = " e Value  is Greatest", e
    elif int (f) > int (e) and int (f) > int (g):
        greatest = " f  Value  is Greatest", f 
    elif int(g) > int (f) and int (g) > int (e):
        greatest = " g Value  is Greatest", g
    elif e == f and f == g and g == e:
        greatest = " Three Values are Equal",e,f,g
    else:
        greatest = "Two  Values  are equal"
    context = {"greatest":greatest}
    return render(request,"directory/greatest1.html",context)