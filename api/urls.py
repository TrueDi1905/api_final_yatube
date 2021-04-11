from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import PostViewSet, CommentViewSet, FollowList, GroupList

router = DefaultRouter()
router.register('', PostViewSet, basename='posts')
router.register(r'(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('posts/', include(router.urls)),
    path('follow/', FollowList.as_view()),
    path('group/', GroupList.as_view()),
]
