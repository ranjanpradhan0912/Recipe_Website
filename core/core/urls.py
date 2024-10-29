"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from accounts.views import *
from about.views import *
from contacts.views import *
from recipe_blog.views import *

# from django.conf.urls.static import static
# from django.contrib import settings
# # from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home"),
    path('accounts/',accounts,name="accounts"),
    path('login_page/',login_page,name="login_page"),
    path('logout_page/',logout_page,name="logout_page"),
    path('about/',about,name="about"),
    path('contact/',contacts,name="contacts"),
    path('recipe_blog/',recipe_blog,name="recipe"),
    path('delete_recipe/<id>/',delete_recipe,name="delete_recipe"),
    path('update_recipe/<id>/',update_recipe,name="update_recipe"),
]


# if settings.DEBUG:
#     urlpatterns +=static(settings.MEDIA_URL,
#                         document_root=settings.MEDIA_ROOT)

