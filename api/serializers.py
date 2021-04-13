from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

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

    user = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all(),
        default=serializers.CurrentUserDefault())

    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя")
        return data

    class Meta:
        fields = ('following', 'user')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['following', 'user'],
            )
        ]


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title')
        model = Group
