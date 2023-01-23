from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.UserAPIView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetailAPIView.as_view(), name='user-details')
]
