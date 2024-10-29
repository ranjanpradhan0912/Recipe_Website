from django.shortcuts import render
from django.http import HttpResponse
from home.models import *
from recipe_blog.models import *

#Main Logical Part

# def home(request):
#  return HttpResponse("Home Page")

#CRUD OPERATION


def home(request):
 recipes=Recipe.objects.all()
 
 return render(request,"home/index.html",context={'recipes':recipes,'page':'Home'})


