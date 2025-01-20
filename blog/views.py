


from django.shortcuts import render,redirect

from django.urls import reverse

from django.http import HttpResponse
import logging

# Create your views here.
posts=[
        {'id':1,'title': 'Post 1', 'content': 'content of the post 1'},
        { 'id':2,'title': 'Post 2', 'content': 'content of the post 2'},
        { 'id':3,'title': 'Post 3', 'content': 'content of the post 3'},
        { 'id':4,'title': 'Post 4', 'content': 'content of the post 4'}
    ]

def index(request):
    blog_title="Latest Posts"
    return render(request,'index.html',{'blog_title':blog_title , 'posts':posts}, )


def detail(request, post_id):
    post=next((item for item in  posts if item['id']==int(post_id)),None)
    # logger=logging.getLogger("testing")
    # logger.debug(f'post variable is{post}')
    return render(request,'detail.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse("blog:new_url_page"))

def new_url(request):
    return HttpResponse("This is new URL page")


def custom_page_not_found(request, exception):
    return render(request,'404.html',ststus=404)









