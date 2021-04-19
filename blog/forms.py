from django import forms
from .models import *

class PostForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new blog'}))
    description=forms.Textarea()

    class Meta:
        model = Post
        fields=('title','description')