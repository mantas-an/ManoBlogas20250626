from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views.generic import ListView, DetailView, CreateView
from myapp.models import Post
from .forms import PostForm


# Create your views here.

class ListOfPosts(ListView):
    model = Post
    template_name = 'list_of_posts.html'
    context_object_name = 'posts'


class DetailPostView(DetailView):
    model = Post  # Still Post, but fetches Post.objects.get(pk=1) DetailView sita suteikia
    template_name = 'detail_post_view.html'
    context_object_name = 'post'


class AddPosts(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_posts.html'
    context_object_name = 'add_posts'
    #fields = ['title', 'content', 'author'] <-- Nebenaudosim, nes turime form.py clase ir perduodam info i sia klase su form_clas=PostForm #arba galime naudoti fields=  '__all__'





