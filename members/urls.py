from django.contrib.auth import views
from django.contrib.auth.views import LogoutView
from django.urls import path

from members.views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),


]