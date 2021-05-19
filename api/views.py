from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from message_board.models import Post
from .serializers import MessageSerializer

class MessageApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = MessageSerializer