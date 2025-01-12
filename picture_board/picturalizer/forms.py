from django import forms
from .models import Image, Comment
from django.core.exceptions import ValidationError

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture', 'author', 'title']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author']
        labels = {
            'text':'新規コメント',
            'author':'送り主名'
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     text = cleaned_data.get('text', '')
    #     author = cleaned_data.get('author', '')
    #     if not text == 'a':
    #         raise ValidationError('txtgatigau')
    #     if not author == 'a':
    #         raise ValidationError('authorgatigau')
