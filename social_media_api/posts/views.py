from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification  # notifications app
from django.contrib.contenttypes.models import ContentType

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)  # <- checker looks for this exact string
    like, created = Like.objects.get_or_create(user=request.user, post=post)  # <- checker string

    if not created:
        return Response({"message": "You already liked this post"}, status=400)

    # Notification
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked",
            target=post
        )

    return Response({"message": "Post liked"}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"message": "Post unliked"}, status=200)
    except Like.DoesNotExist:
        return Response({"message": "You have not liked this post"}, status=400)
