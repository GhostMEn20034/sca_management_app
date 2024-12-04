from rest_framework.routers import SimpleRouter

from .views import TargetViewSet


router = SimpleRouter()
router.register(r'targets', TargetViewSet)

urlpatterns = router.urls
