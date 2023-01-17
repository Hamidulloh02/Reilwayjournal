from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Category,Video




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at', 'profile','category')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('video_title','video_link')