from django import forms
from .models import Billboard, Comment

#
class BillboardForm(forms.ModelForm):
    class Meta:
        model = Billboard
        fields = ['title', 'author', 'content', 'date_published']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'author', 'date', 'billboard']