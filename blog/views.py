


from django.shortcuts import render,redirect

from django.urls import reverse

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')


def detail(request, post_id):
    return render(request,'detail.html')

def old_url_redirect(request):
    return redirect(reverse("blog:new_url_page"))

def new_url(request):
    return HttpResponse("This is new URL page")









