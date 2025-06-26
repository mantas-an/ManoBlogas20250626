from django.contrib import admin
from django.core.checks import register

from myapp.models import Post

# Register your models here

admin.site.register(Post)