from django.contrib.auth import views
from django.urls import path

from myapp.views import ListOfPosts, DetailPostView, AddPosts, UpdatePost

urlpatterns = [

    path('', ListOfPosts.as_view(), name='list_of_posts'),
    path('posts/<int:pk>/', DetailPostView.as_view(), name='detail_post_view'),
    path('add_posts/', AddPosts.as_view(), name='add_posts'),
    path('posts/edit/<int:pk>/', UpdatePost.as_view(), name='update_post'),

]