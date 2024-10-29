from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login_page")

def recipe_blog(request):

 if request.method=="POST":
  data=request.POST
  recipe_name=data.get('recipe_name')
  recipe_desc=data.get('recipe_desc')
  recipe_image=request.FILES.get('recipe_image')
  user=request.user

  Recipe.objects.create(
  user=user,
  recipe_name=recipe_name,
  recipe_desc=recipe_desc,
  recipe_image=recipe_image
  )
  return redirect('/recipe_blog')
 queryset=Recipe.objects.filter(user=request.user)

 if request.GET.get('search'):
   queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))

 return render(request,"recipe_blog/index.html",context={"page":'recipe_blog',"recipes":queryset})



def delete_recipe(request,id):
 queryset=Recipe.objects.get(id=id)
 queryset.delete()
 return redirect('/recipe_blog')


  
def update_recipe(request,id):
 queryset=Recipe.objects.get(id=id)
 if request.method=="POST":
   data=request.POST
   recipe_name=data.get('recipe_name')
   recipe_desc=data.get('recipe_desc')
   recipe_image=request.FILES.get('recipe_image')

   queryset.recipe_name=recipe_name
   queryset.recipe_desc=recipe_desc
   if recipe_image:
    queryset.recipe_image=recipe_image
   queryset.save()
   return redirect('/recipe_blog')
 return render(request,"recipe_blog/update_recipe.html",context={"page":'update_recipe',"recipe":queryset})


  
