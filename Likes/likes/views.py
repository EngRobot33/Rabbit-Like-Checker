import requests
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .producer import publish
from .serializers import *


class PostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostUserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PostUserSerializer
    queryset = PostUser.objects.all()

    @api_view(['GET'])
    def like(request, pk, format=None):
        query = {'username': 'admin'}
        req = requests.get('http://127.0.0.1:8000/users', params=query)
        data = req.json()
        print(data)

        try:
            for i in range(len(data)):
                if data[i]['id']:
                    postuser = PostUser.objects.create(user_id=data[i]['id'], post_id=pk)
                    postuser.save()
                    publish('post_liked', pk)
                    print('PostUser created.')
                    return Response('Post liked...', status=status.HTTP_201_CREATED)
        except:
            return Response("Post liked...", status=status.HTTP_400_BAD_REQUEST)
