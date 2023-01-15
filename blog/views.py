from django.http import HttpResponse
from django.shortcuts import render
from multiprocessing import context
from .models import Post
from .forms import Postforms

def index(request):
    db = Post.objects.all()
    context ={
        'title':'Blog',
        'heading':'Blog',
        'subheading': 'postingan',
        'post' : db,
    }
    # context = {
    #     'Judul' : 'AppBlog',
    #     'h1' : 'Django',
    #     'menu' : [['/', 'Home'], ['/blog/recent', 'Recent'], ['/blog/post', 'Post']]
    # }
    return render(request,'blog/index.html', context)

def recent(request):
    return HttpResponse("<h1>RECENT BLOG</h1>")

def post(request):
    return HttpResponse("<h1>INI ISINYA POST</h1>")

def about(request):
    return HttpResponse("<h1>ABOUT BLOG</h1>")

def form(request):
    classform = forms.classform(request.POST or None)

    if request.method == 'POST':
        if classform.is_valid():
            classform.save()
            return HttpResponsedirect('/blog/')
            
    context = {
        'heading' : 'Home',
        'classform' :classform
    }
    return render(request, 'form.html', context)

def delete(request, id):
    Post.objects.filter(id=id).delete()
    return HttpResponseRedirect('/blog/')

def update(request, id):
    updt = Post.objects.get(id=id)
    data = {
        'title' : updt.title,
        'body' : updt.body,
        'email' : updt.email,
    }
    classform = forms.classform(request.POST or None, initial=data, instance=updt)

    if request.method == 'POST':
        if classform.is_valid():
            classform.save()
            return HttpResponseRedirect('/blog/')

    context = {
        'heading': 'updt',
        'classform': classform
    }
    return render(request, 'form.html', context)





    # if request.method == 'POST':
    #     print("ini adalah method post")
    #     context['nama'] == request.POST['nama']
    #     context['alamat'] == request.POST['alamat']
    #     context['namac'] == request.POST['namac']
    #     context['alamat'] == request.POST['alamat']
    # else:
    if request.POST.get('nama') and request.POST.get('alamat') and request.POST.get('tgl_lahir') and request.POST.get('email'):
            post = Post()
            post.nama = request.POST.get('nama')
            post.alamat = request.POST.get('alamat')
            post.tgl_lahir = request.POST.get('tgl_lahir')
            post.email = request.POST.get('email')
            post.save()

            return render(request, 'form/index.html')
    else:
        print("ini adalah method get")
    return render(request, 'form.html', context)