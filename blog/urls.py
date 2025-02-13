"""
URL configuration for myapp project.

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
from .import views


handler404 ='myapp.views.custom_page_not_found'

app_name='blog'

urlpatterns = [
    path("",views.index, name="index"),
    path("details/<int:post_id>",views.detail,name="detail"),
    path("old_url",views.old_url_redirect,name="old_url"),
    path("new_url_page",views.new_url,name="new_url_page")
]
