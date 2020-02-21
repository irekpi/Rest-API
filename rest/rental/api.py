from rest_framework import routers
from . import api_views as app_views


router = routers.DefaultRouter()
router.register(r'friends', app_views.FriendViewset)
router.register(r'belongings', app_views.BelongingViewset)
router.register(r'borrowings', app_views.BorrowedViewset)