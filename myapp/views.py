from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView, DetailView

from myapp.models import Post


# Create your views here.

class ListOfPosts(ListView):
    model = Post
    template_name = 'list_of_posts.html'
    context_object_name = 'posts'

class DetailPostView(DetailView):
    model = Post  # Still Post, but fetches Post.objects.get(pk=1) DetailView sita suteikia
    template_name = 'detail_post_view.html'
    context_object_name = 'post'


