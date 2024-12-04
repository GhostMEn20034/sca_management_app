from rest_framework.routers import SimpleRouter

from .views import SpyCatViewSet

router = SimpleRouter()
router.register(r'spy-cats', SpyCatViewSet)

urlpatterns = router.urls
