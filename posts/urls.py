from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from posts.views import PostsPerUserViewSet
from .views import PostViewSet

from users.urls import router as user_router

router = DefaultRouter()
router.register(r'posts', PostViewSet, base_name='posts')

user_posts = NestedSimpleRouter(user_router, r'users', lookup='user')
user_posts.register(r'posts', PostsPerUserViewSet, base_name='user-posts')
