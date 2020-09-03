from . models import Friend, Belonging, Borrowed
from . serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class FriendViewset(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]


class BelongingViewset(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer
    permission_classes = [AllowAny]


class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer
    permission_classes = [IsAdminUser]