from django import forms
from .models import Post, Comment
class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text','type_tag')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)