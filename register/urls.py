
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("success/", views.success, name="success"),
    path("login/", views.login, name="login"),
    path("welcome/", views.welcome, name="welcome"),
    path("logout/", views.logout, name="logout"),
]
