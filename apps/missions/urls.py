from rest_framework.routers import SimpleRouter

from .views import MissionViewSet


router = SimpleRouter()
router.register(r'missions', MissionViewSet)

urlpatterns = router.urls
