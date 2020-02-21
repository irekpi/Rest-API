from . import models
from . import serializers
from .permissions import IsOwner
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail


class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer
    # permission_classes = [IsOwner]


class BelongingViewset(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongignSerializer


class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer

    @action(detail=True, url_path='remind', methods=['post'])
    def remind_single(self, request, *args, **kwargs):
        obj = self.get_object()
        send_mail(
            subject=f'return the { obj.what_name }',
            message=f'you need to do it asap',
            from_email="admin@admin.admin",
            recipient_list=[obj.to_who.email],
            fail_silently=False,
        )
        return Response('email sent')


class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
