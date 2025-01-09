from django.db import models
import PIL

class Image(models.Model):
    picture = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, default='名無し')

    def __str__(self):
        return self.title


class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')  # Imageモデルとの関連
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, default='名無し')

