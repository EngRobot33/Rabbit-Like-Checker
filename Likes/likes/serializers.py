from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostUser
        fields = '__all__'
