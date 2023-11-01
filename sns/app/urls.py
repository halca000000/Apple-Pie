from django.urls import path
from . import views

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
]
