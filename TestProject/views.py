from django.http import HttpResponse
from django.shortcuts import render


def hello(request,name):
    return render(request,"home.html",{"name":name})
    #return HttpResponse("<b>Hello "+name+"</b>")