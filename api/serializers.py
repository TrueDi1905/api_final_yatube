from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Comment, Post, Follow, Group, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    def validate_following(self, value):
        user = self.context['request'].user
        following = get_object_or_404(User, username=value)
        if user == following:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя")
        follow_check = Follow.objects.filter(
            user=user, following=following).exists()
        if follow_check:
            raise serializers.ValidationError(
                f"Вы уже подписаны на {following.username}")
        return value

    class Meta:
        fields = ('following', 'user')
        model = Follow


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title')
        model = Group
