"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.index , name = "index"),
    path('about',views.about, name = "about"),
    path('register',views.user_register, name = "register"),
    path('login',views.user_login, name = "login"),
    path('logout',views.user_logout, name = "logout"),
    path('post_blog',views.user_blogpost, name = "post_blog"),
    path('blog_detail/<int:id>',views.blog_detail, name = "blog_detail"),
    path('delete/<int:id>',views.delete, name = "delete"),
    path('edit/<int:id>',views.edit, name = "edit"),
   




   

]
