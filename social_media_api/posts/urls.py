from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed, like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns += [
    path('feed/', feed, name='user-feed'),
    path('posts/<int:pk>/like/', like_post, name='like-post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post'),
]

urlpatterns += router.urls
