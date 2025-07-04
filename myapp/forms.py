from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = ['title', 'content', 'author'] - panaikinome authors,nes nera logikos ji rodyti dabar creatinant posta taip pat ir is widgets
        fields = ['title', 'content', 'header_image']

        #widget = styling
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Posto pavadinimas'}), #we will pass css class, sita vieta bus naudojama bootsrapui formoms
            'content': forms.Textarea(attrs={'class': 'form-control'}), #we will pass css class sita vieta bus naudojama bootsrapui formoms
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control'}), #we will pass css class sita vieta bus naudojama bootsrapui formoms
            #'author': forms.Select(attrs={'class': 'form-control'}), #we will pass css class sita vieta bus naudojama bootsrapui formoms

            # P.S kad nereiketu viso sito s su widgets, geriau naudoti CRISPY
        }




class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        #widget = styling
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Posto pavadinimas'}), #we will pass css class, sita vieta bus naudojama bootsrapui formoms
            'content': forms.Textarea(attrs={'class': 'form-control'}), #we will pass css class sita vieta bus naudojama bootsrapui formoms
            #'author': forms.Select(attrs={'class': 'form-control'}), #we will pass css class sita vieta bus naudojama bootsrapui formoms
        }