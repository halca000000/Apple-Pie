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
#さわ追加
from django.shortcuts import render,get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostCreationForm, CommentCreationForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

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
   
   #さわ追加
@method_decorator(login_required, name = 'dispatch')
class NavView(ListView):
    template_name = 'App_Foldeer_HTML/nav.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')
        return queryset
    
@method_decorator(login_required, name = 'dispatch')
class DetailView(DetailView):
    model = Post
    template_name = 'App_Foldeer_HTML/detail.html'

@method_decorator(login_required, name = 'dispatch')
class PostCreatedView(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'App_Foldeer_HTML/form.html'
    success_url = reverse_lazy('timelines:index')

    def form_valid(self, form):
        pd = form.save(commit=False)
        pd.user = self.request.user
        pd.save()
        return super().form_valid(form)
    
@method_decorator(login_required, name = 'dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'App_Foldeer_HTML/delete.html'
    success_url = reverse_lazy('timelines:index')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    
@method_decorator(login_required, name = 'dispatch')
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'App_Foldeer_HTML/update.html'
    form_class = PostCreationForm
    success_url = reverse_lazy('timelines:detail')

@method_decorator(login_required, name = 'dispatch')
class CommentCreateView(CreateView):
    model = Comment
    template_name = 'App_Foldeer_HTML/comment.html'
    form_class = CommentCreationForm
    success_url = reverse_lazy('timelines:detail')

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post  
        comment.user = self.request.user
        comment.save()
        return redirect('timelines:detail', pk=post.pk)

class UserPostView(ListView):
    template_name = 'App_Foldeer_HTML/userpost.html'

    def get_queryset(self):
        user_id = self.kwargs['user']
        queryset = Post.objects.filter(user = user_id)
        return queryset