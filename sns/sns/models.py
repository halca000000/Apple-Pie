from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # プロフィール画像をavatarとして設定
    avatar = models.ImageField(blank=True, null=True)  
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] 

# Create your models here.
class Post(models.Model):
    icon = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='ユーザー')
    created_at = models.DateField(auto_now_add=True, verbose_name='投稿日時')
    text = models.TextField(verbose_name='本文')
    image = models.ImageField(upload_to='images', null=True, blank=True)#さわ追加

    def __str__(self):
        return self.text

class Comment(models.Model):
    text = models.TextField(verbose_name='コメント')
    created_at = models.DateField(auto_now_add=True, verbose_name='返信日時')
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='対象の投稿')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='ユーザー')

    def __str__(self):
        return self.text