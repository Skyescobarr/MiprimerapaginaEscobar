
from django import forms

from .models import Post, Category, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'email', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }

class PostSearchForm(forms.Form):
    query = forms.CharField(label='Buscar Post por Título', max_length=100)