from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from account.models import Vendor, HistoricalPerformance
from django_filters.rest_framework import DjangoFilterBackend
from account.serializers import VendorSerializer, HistoricalPerformanceSerializer

# Create your views here.


class VendorViewSet(ModelViewSet):
    '''
    APIs to View/Create/Update/Delete Vendor
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = "__all__"


class HistoricalPerformanceViewSet(ModelViewSet):
    '''
    API to get HistoricalPerformance of the Vendor of provided vendor id
    '''
    permission_classes = (IsAuthenticated,)
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    http_method_names = ['get',]

    def get_queryset(self):
        return self.queryset.filter(vendor_id=self.request.parser_context.get('kwargs', {}).get('vendor_id'))