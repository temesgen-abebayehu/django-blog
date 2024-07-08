from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'index.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post':post})