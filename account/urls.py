from django.urls import path, include
from account import views
from django.contrib.auth import views as auth

urlpatterns = [
    #path("login/", views.user_login, name="login"),
    path("login/", auth.LoginView.as_view, name="login"),
    path("logout/", auth.LogoutView.as_view, name="logout"),
]