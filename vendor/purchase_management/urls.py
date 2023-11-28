from rest_framework.routers import DefaultRouter
from django.urls import path
from purchase_management.views import PurchaseOrderViewSet, AcknowledgePurchaseOrder

router = DefaultRouter()

router.register(r'', PurchaseOrderViewSet, basename='purchase-order')

urlpatterns = router.urls

urlpatterns += [
    path('<int:pk>/acknowledge', AcknowledgePurchaseOrder.as_view({'patch': 'update'}), name='acknowledge'),
]