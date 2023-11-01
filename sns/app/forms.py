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

#プロフィール2
class ProfileForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
       super(ProfileForm, self).__init__(*args, **kwargs)
       
       for field in self.fields.values():  # bootstrapで使用するform-controlクラス
           field.widget.attrs['class'] = 'form-control'
           
   class Meta:
       model = User
       fields = ('username', 'email', 'avatar')
       help_texts = {
           'username': None,
           'email':None,
       }