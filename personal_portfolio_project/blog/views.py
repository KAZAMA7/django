from django.shortcuts import render
from .models import Blogs

def blog_home(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog/home.html', {'blogs':blogs})

