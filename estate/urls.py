from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstateViewSet

router = DefaultRouter()
router.register(r'estates', EstateViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = router.urls
