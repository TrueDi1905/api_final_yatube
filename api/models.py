from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.text import slugify
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        "Дата публикации", auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    group = models.ForeignKey('Group', on_delete=models.CASCADE,
                              related_name="posts", blank=True, null=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.fields.SlugField(unique=True,
                                   verbose_name="Уникальный адрес", blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Group, self).save(*args, **kwargs)


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="following")

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'following'],
                name='unique_fields',)
        ]


class FollowViewSetCustom(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    """
    A viewset that provides default `create()` and `list()` actions.
    """
    pass


class GroupViewSetCustom(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    """
    A viewset that provides default `create()` and `list()` actions.
    """
    pass
