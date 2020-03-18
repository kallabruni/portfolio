from django.shortcuts import render
from .models import Blog_post

def all_blogs(request):
    blog_posts = Blog_post.objects.all()
    return render(request, 'blog/all_blogs.html', {'blog_post':blog_posts})
