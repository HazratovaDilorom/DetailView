from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView
from  .models import Post



class  Home(ListView):
    template_name='index.html'
    queryset=Post.objects.all()
    context_object_name='posts'

class Temp(DetailView):
    model = Post
    template_name='blog-single-html'
    context_object_name='post'
  