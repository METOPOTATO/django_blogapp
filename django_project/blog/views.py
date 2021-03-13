from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Linh',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted':'August 2,2020'
    },
        {
        'author': 'James',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted':'August 3,2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')