from .serializers import PostSerializer, UserSerializer,CategorySerializer,VideoSerializer
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics
from .models import Post,Category,Video
from .permissions import IsAuthorOrReadOnly


# Create your views here.

class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True).order_by('-id')
    serializer_class = CategorySerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_active=True).order_by('-id')
    serializer_class = PostSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class VideoViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoListAPIView(ModelViewSet):
    queryset = Video.objects.filter(is_active=True)
    serializer_class = VideoSerializer