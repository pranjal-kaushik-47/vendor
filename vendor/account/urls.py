from rest_framework.routers import DefaultRouter
from account.views import VendorViewSet

router = DefaultRouter()

router.register(r'', VendorViewSet, basename='vendor')

urlpatterns = router.urls