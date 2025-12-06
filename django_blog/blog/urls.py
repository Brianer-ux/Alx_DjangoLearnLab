# blog/urls.py
from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    CommentUpdateView, CommentDeleteView, CommentCreateView
)
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path("post/new/", PostCreateView.as_view(), name="post-create"),           # singular "post"
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"), # rename "edit" → "update"
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path('posts/<int:post_id>/comments/new/', CommentCreateView, name='add-comment'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
