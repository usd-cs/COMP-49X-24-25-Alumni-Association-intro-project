from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']  # Only include 'content' since 'title' is removed
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter content',
                'rows': 4
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a comment...',
                'rows': 2
            })
        }
