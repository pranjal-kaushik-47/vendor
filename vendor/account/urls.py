from rest_framework.routers import DefaultRouter
from django.urls import path
from account.views import VendorViewSet, HistoricalPerformanceViewSet

router = DefaultRouter()

router.register(r'', VendorViewSet, basename='vendor')
router.register(r'(?P<vendor_id>\d+)/performance', HistoricalPerformanceViewSet, basename='vendor')

urlpatterns = router.urls