from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
  template_name = "app/index.html"

from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy

from .forms import SignUpForm


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
