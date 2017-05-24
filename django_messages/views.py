
from .models import Message
from django_messages.utils import format_quote, get_user_model, get_username_field
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from .serializer import MessageSerializer

User = get_user_model()

class MesssageViewset(viewsets.GenericViewSet):
    
    def list(self, request):
        message_list = Message.objects.inbox_for(request.user)
        message_serializer = MessageSerializer(message_list, many=True)

        return Response(message_serializer.data)
    
    def create(self, request):
        import datetime
        msg_data = {}
        
        msg_data['subject'] = request.data.get('subject')
        msg_data['body'] = request.data.get('body')
        msg_data['recipient'] = request.data.get('recipient')
        msg_data['sender'] = request.user.id

        msg_serializer = MessageSerializer(data=msg_data)
        msg_serializer.is_valid(raise_exception=True)

        msg_serializer.save()

        return Response(status=status.HTTP_201_CREATED)
        
    @list_route(methods=['GET'], url_path='outbox')
    def outbox(self, request):
        message_list = Message.objects.outbox_for(request.user)
        message_serializer = MessageSerializer(message_list, many=True)

        return Response(message_serializer.data)