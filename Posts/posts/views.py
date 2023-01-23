from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .producer import publish


class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Post.objects.all()
        serializer = PostSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('post_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Post.objects.get(pk=pk)
        serializer = PostSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        product = Post.objects.get(pk=pk)
        serializer = PostSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('post_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        product = Post.objects.get(pk=pk)
        product.delete()
        publish('post_deleted', pk)
        return Response('Post deleted.')


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)


class UserDetailAPIView(APIView):
    def get_user(self, pk):
        try:
            User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
