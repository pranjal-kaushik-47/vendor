from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from purchase_management.models import PurchaseOrder
from django_filters.rest_framework import DjangoFilterBackend
from purchase_management.serializers import PurchaseOrderSerializer, AcknowledgmentSerializer

# Create your views here.


class PurchaseOrderViewSet(ModelViewSet):
    '''
    APIs to View/Create/Update/Delete PurchaseOrders
    '''
    permission_classes = (IsAuthenticated,)
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['vendor_id']


class AcknowledgePurchaseOrder(ModelViewSet):
    '''
    API to update the acknowledgment_date of a PurchaseOrder
    PurchaseOrder must be associated with the logged in vendor
    '''
    permission_classes = (IsAuthenticated,)
    queryset = PurchaseOrder.objects.all()
    serializer_class = AcknowledgmentSerializer
    http_method_names = ['patch',]

    def get_queryset(self):
        return self.queryset.filter(vendor_id=self.request.user.id)