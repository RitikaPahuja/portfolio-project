from django.shortcuts import render ,get_object_or_404
from .models import blogs

# Create your views here.

def allblogs(request):
    blog_s = blogs.objects
    return render(request,'blogs/home.html',{'allblogs':blog_s})

def detail(request,blog_id):
    detail_blog = get_object_or_404(blogs,pk=blog_id)
    return render(request,'blogs/detail.html',{'blog':detail_blog})
