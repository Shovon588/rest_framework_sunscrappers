from . models import Friend, Belonging, Borrowed
from . serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer

from rest_framework import viewsets


class FriendViewset(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class BelongingViewset(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer


class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer