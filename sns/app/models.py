from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    
# Create your models here.
class Post(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name='投稿日時')
    text = models.TextField(verbose_name='ユーザー')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザー')

    def __str__(self):
        return self.text

class Comment(models.Model):
    text = models.TextField(verbose_name='コメント')
    created_at = models.DateField(auto_now_add=True, verbose_name='返信日時')
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='対象の投稿')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザー')

    def __str__(self):
        return self.text