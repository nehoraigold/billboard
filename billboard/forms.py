from django import forms
from .models import Billboard, Comment

#
class BillboardForm(forms.ModelForm):
    class Meta:
        model = Billboard
        fields = ['title', 'author', 'content', 'date_published']
        widgets = {
            'author': forms.TextInput(attrs={'disabled': True})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'author', 'date', 'billboard']