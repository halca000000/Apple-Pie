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

# Create your views here.

class IndexView(TemplateView):
  template_name = "app/index.html"

class HomeView(TemplateView):
    template_name = "app/home.html"

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "app/signup.html"
    success_url = reverse_lazy("app:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

#追加
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/profile.html')