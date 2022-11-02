from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newpost/", views.new_post, name="post"),
    path("post/<int:pk>/", views.view_post, name="view_post"),
    path("posts/edit/<int:pk>", views.edit_post, name="edit_post"),
    path("posts/delete/<int:pk>", views.delete_post, name="delete_post"),
]
