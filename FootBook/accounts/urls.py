from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registration_func, name="registration"),
    path("login/", views.login_func, name="login"),
    path("logout/", views.logout_func, name="logout"),
]
