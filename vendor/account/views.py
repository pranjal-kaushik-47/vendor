from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from account.models import Vendor
from django_filters.rest_framework import DjangoFilterBackend
from account.serializers import VendorSerializer

# Create your views here.


class VendorViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = "__all__"