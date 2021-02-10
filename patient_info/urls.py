from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PDocViewSet

router = DefaultRouter()
router.register(r'pdocs', PDocViewSet, basename='pdoc')
urlpatterns = router.urls
