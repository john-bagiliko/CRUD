"""
By: John Bagiliko
Year: 2019
"""
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
