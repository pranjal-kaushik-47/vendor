from rest_framework.routers import DefaultRouter
from purchase_management.views import PurchaseOrderViewSet

router = DefaultRouter()

router.register(r'', PurchaseOrderViewSet, basename='purchase-order')

urlpatterns = router.urls