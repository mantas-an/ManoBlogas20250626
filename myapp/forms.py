from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

        #widget = styling
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Posto pavadinimas'}), #we will pass css class, sita vieta bus naudojama bootsrapui formoms
            'content': forms.Textarea(attrs={'class': 'form-control'}), #we will pass css class sita vieta bus naudojama bootsrapui formoms
            'author': forms.Select(attrs={'class': 'form-control'}), #we will pass css class sita vieta bus naudojama bootsrapui formoms
        }