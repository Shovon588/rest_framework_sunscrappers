from rest_framework import routers

from rental import viewsets

router = routers.DefaultRouter()
router.register('friends', viewsets.FriendViewset)
router.register('belongings', viewsets.BelongingViewset)
router.register('borrowings', viewsets.BorrowedViewSet)