from django import forms
from .models import Image, Comment
from django.core.exceptions import ValidationError
from PIL import Image as PILImage

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture', 'author', 'title']

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if not picture:
            raise ValidationError('画像ファイルが必要です。')
        try:
            img = PILImage.open(picture)
            img.verify()  # 画像の整合性を検証（画像ファイルでない場合はエラーになる）
        except (IOError, SyntaxError):
            raise ValidationError('無効な画像ファイルです。画像ファイルをアップロードしてください。')

        return picture


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
