from django.shortcuts import render
from django.views.generic import TemplateView

from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
#ログイン
from .forms import SignUpForm
#プロフィール
from django.views import View
from django.shortcuts import render, redirect
#ログイン
from .forms import SignUpForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
#プロフィール2
from django.views.generic.edit import CreateView, UpdateView
from .forms import LoginForm , ProfileForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import CustomUser


# Create your views here.

class IndexView(TemplateView):
  template_name = "App_Folder_HTML/index.html"

class HomeView(TemplateView):
    template_name = "App_Folder_HTML/home.html"

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "App_Folder_HTML/signup.html"
    success_url = reverse_lazy("app:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

#追加
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'App_Folder_HTML/profile.html')
    
#ログイン画面
class UserLoginView(LoginView):  # 追加
   template_name = 'App_Folder_HTML/login.html'
   authentication_form = LoginForm
       
class UserLogoutView(LogoutView): # 追加
   pass

class ProfileEditView(LoginRequiredMixin, UpdateView): # 追加
   template_name = 'accounts/edit_profile.html'
   model = CustomUser
   form_class = ProfileForm
   success_url = '/accounts/edit_profile/'
   def get_object(self):
       return self.request.user

class UserListView(LoginRequiredMixin, ListView): # 追加
   template_name = 'accounts/userlist.html'
   model = CustomUser
      
   def get_queryset(self):       
       return CustomUser.objects.all()