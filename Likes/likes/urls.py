from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('postusers', views.PostUserViewSet, basename='postusers')

urlpatterns = [
    path('', include(router.urls))
]
