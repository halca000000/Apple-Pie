from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#ログイン
from django.contrib.auth.forms import AuthenticationForm 

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

#
class LoginForm(AuthenticationForm):  # 追加
   username = forms.CharField(label='ユーザーネーム') 
   password = forms.CharField(label='パスワード', widget=forms.PasswordInput) 