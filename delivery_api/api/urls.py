from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'positions', views.PositionViewSet)
urlpatterns = router.urls
