from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field



# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - "{self.author}"'

    def get_absolute_url(self):
        #return reverse('detail_post_view', args=(str(self.id)) ) jeigu norime grazinti i pati posta
        return reverse('list_of_posts') #jei norime tiesiog grazinti i pagrindini puslapi! veikia! ir paprasciau