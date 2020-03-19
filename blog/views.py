from django.shortcuts import render
from .models import Blog_post

def all_blogs(request):
    blog_posts = Blog_post.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blog_posts':blog_posts})
