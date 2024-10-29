from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


#Main Logical Part

# def accounts(request):
#  return HttpResponse("Accounts page")

def accounts(request):
 if request.method=="POST":
   first_name=request.POST.get('first_name')
   last_name=request.POST.get('last_name')
   username=request.POST.get('username')
   user_password=request.POST.get('user_password')
  
   user=User.objects.filter(username=username)

   if user.exists():
      messages.info(request, "Username already exists")
      return redirect('/accounts/')
   
   user=User.objects.create(
     first_name=first_name,
     last_name=last_name,
     username=username  
   )
   user.set_password(user_password)
   user.save()
   messages.info(request, "Account created Successfully")

   return redirect('/accounts/')


 return render(request,'accounts/index.html',context={"page":'Register'})

def login_page(request):
  if request.method=="POST":
   username=request.POST.get('username')
   user_password=request.POST.get('user_password')
   print(username)

   if not User.objects.filter(username=username).exists():
     messages.info(request, "Invalid username")
     return redirect('/login_page/')
   
   user=authenticate(username=username,password=user_password)
   if user is None:
     messages.error(request,"Invalid password")
     return redirect('/login_page/')
   else:
     login(request,user)
     return redirect('/recipe_blog/')
   
  return render(request,'accounts/login.html',context={"page":'Login'})


def logout_page(request):
  logout(request)
  return redirect('/login_page/')


