from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters

from .models import Comment, Post, Follow, Group, \
    FollowViewSetCustom, GroupViewSetCustom
from .serializers import CommentSerializer, PostSerializer, \
    FollowSerializer, GroupSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsOwnerOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    ]
    filterset_fields = ['group', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsOwnerOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id',))
        serializer.save(author=self.request.user,
                        post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments


class FollowViewSet(FollowViewSetCustom):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'following__username', ]

    def get_queryset(self):
        return Follow.objects.filter(
            following__username=self.request.user.username
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(GroupViewSetCustom):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)
