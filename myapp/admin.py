from django.contrib import admin
from django.core.checks import register
from myapp.models import Post, Profile

# Register your models here

admin.site.register(Post)
admin.site.register(Profile)