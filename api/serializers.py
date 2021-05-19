from rest_framework.serializers import ModelSerializer
from message_board.models import Post

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['text']
    