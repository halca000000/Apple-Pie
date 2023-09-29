from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
  path('top/', views.IndexView.as_view(), name='index'),
]

urlpatterns = [
    path('top/', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('home/', views.HomeView.as_view(), name="home"),
]