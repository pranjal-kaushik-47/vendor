from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from purchase_management.models import PurchaseOrder
from django_filters.rest_framework import DjangoFilterBackend
from purchase_management.serializers import PurchaseOrderSerializer

# Create your views here.


class PurchaseOrderViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['vendor_id']