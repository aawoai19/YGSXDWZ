# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home.html')

def plus(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))