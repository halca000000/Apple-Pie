from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
  path('top/', views.IndexView.as_view(), name='index'),
]