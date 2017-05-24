
from .models import Message
from django_messages.utils import format_quote, get_user_model, get_username_field
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import MessageSerializer

User = get_user_model()

class MesssageViewset(viewsets.GenericViewSet):
    
    def list(self, request):
        message_list = Message.objects.inbox_for(request.user)
        message_serializer = MessageSerializer(message_list, many=True)

        return Response(message_serializer.data)