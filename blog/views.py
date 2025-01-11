


from django.shortcuts import render



from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello, You are at index")


def detail(request, post_id):
    return HttpResponse(f"this is post detail page and the id is {post_id}")









