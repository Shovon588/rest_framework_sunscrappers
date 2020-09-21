from . models import Friend, Belonging, Borrowed
from . serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . permissions import IsOwner


class FriendViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = FriendSerializer

    queryset = Friend.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(owner=self.request.user)
        return query_set


class BelongingViewset(viewsets.ModelViewSet):
    serializer_class = BelongingSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    queryset = Belonging.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(owner=self.request.user)
        return query_set


class BorrowedViewSet(viewsets.ModelViewSet):
    serializer_class = BorrowedSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    queryset = Borrowed.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(owner=self.request.user)
        return query_set

