from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Post


def index(request):

    db=Post.objects.all()
    context = {
        'title' : 'Blog',
        'heading' : 'Blog',
        'subheadin' : 'postingan',
        'post' : db,
        
    }
    return render(request, 'blog/index.html', context)

def recent(request):
    # context = {
    #     'Judul' : 'blog2',
    #     'h1' : 'Python'
    # }
    # return render(request, 'blog/index.html', context)
    return HttpResponse('RECENT BLOG')

    