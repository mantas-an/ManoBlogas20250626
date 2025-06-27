from django.contrib.auth import views
from django.urls import path

from myapp.views import ListOfPosts, DetailPostView

urlpatterns = [

    path('', ListOfPosts.as_view(), name='list_of_posts'),
    path('posts/<int:pk>/', DetailPostView.as_view(), name='detail_post_view'),

]