from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "app"

urlpatterns = [
    path('top/', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('home/', views.HomeView.as_view(), name="home"),
    path('profile/', views.ProfileView.as_view(), name='profile'),#追加
    path('login/', views.UserLoginView.as_view(), name='login'), #ログイン
    path('logout/', views.UserLogoutView.as_view(), name='logout'), #ログアウト 
    path('edit_profile/', views.ProfileEditView.as_view(), name='edit_profile'), #プロフ編集
    path('userlist/', views.UserListView.as_view(), name='userlist'), #ユーザリスト
     #ここからさわはやが追加しました
    path('nav/', views.NavView.as_view(), name="nav"),
    path('detail/',views.PostDeleteView.as_view(), name="detail"),
    path('delete/', views.DeleteView.as_view(), name="delete"),
    path('form/', views.PostCreatedView.as_view(), name="form"),
    path('delete/',views.PostUpdateView.as_view(), name = "update"),
    path('commentcr/', views.CommentCreateView.as_view(), name = "commentcr"),
    path('userpost/',views.UserPostView.as_view(), name = "userpost")

    #ここまでさわはやが追加しました
]
