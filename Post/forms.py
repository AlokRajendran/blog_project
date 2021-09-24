from django.forms import ModelForm
from django import forms

from django.forms import fields, widgets
from .models import Post



class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'Author', 'Contents', 'postcategory')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'Author':forms.Select(attrs={'class':'form-control'}),
            'Contents':forms.Textarea(attrs={'class':'form-control'}),
            'postcategory':forms.Select(attrs={'class':'form-control'}),



        }