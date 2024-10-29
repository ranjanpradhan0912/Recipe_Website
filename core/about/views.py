from django.shortcuts import render
from django.http import HttpResponse


def about(request):
#  return HttpResponse(232)
 return render(request,"about/index.html",context={"page":'About'})


