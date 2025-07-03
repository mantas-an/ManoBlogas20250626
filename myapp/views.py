import bleach
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from myapp.models import Post
from .forms import PostForm, EditForm


# Create your views here.

class ListOfPosts(ListView):
    model = Post
    template_name = 'list_of_posts.html'
    context_object_name = 'posts'
    ordering = ['-created_at'] #si vieta leidzia pateikti postus nuo naujausio is virsaus, defaultu naujausi apacioje, veliau pridesim pagal data




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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # si methoda sukureme, nes pacioj pradzioje buvom leide pasirinkti posto autoriu kai kuriame psota, si methoda sukurus, taip pat reikejo koreguoti ir formas kurias naudojame siame view

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'content']


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('list_of_posts')

