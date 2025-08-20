from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

from .views import feed

urlpatterns = [
    path("feed/", feed, name="feed"),
]
from .views import LikePostView, UnlikePostView

urlpatterns = [
    path("<int:pk>/like/", LikePostView.as_view(), name="like-post"),
    path("<int:pk>/unlike/", UnlikePostView.as_view(), name="unlike-post"),
]