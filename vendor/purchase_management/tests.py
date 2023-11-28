from django.test import TestCase, RequestFactory
from rest_framework.test import force_authenticate
from .views import (
    PurchaseOrderViewSet
)
from .models import (
    PurchaseOrder
)
from account.models import (
    Vendor
)
import datetime as dt


class TestApi(TestCase):
    def setUp(self) -> None:
        self.vendor = Vendor.objects.create(
            name='vendor1xx',
            contact_details='xx123',
            address='address',
            vendor_code='123as'
        )
        self.po = PurchaseOrder.objects.create(
            po_number='123456789',
            vendor=self.vendor,
            estimated_delivery_date=dt.date.today()+dt.timedelta(days=5),
            items={'bag':'a big bag'},
            quantity=5
        )
        self.factory = RequestFactory()

    def test_PurchaseOrderListAPI(self):
        request = self.factory.get(
            'api/purchase_orders/')
        force_authenticate(request, user=self.vendor)
        response = PurchaseOrderViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
    
    def test_PurchaseOrderGetAPI(self):
        request = self.factory.get(
            'api/purchase_orders/')
        force_authenticate(request, user=self.vendor)
        response = PurchaseOrderViewSet.as_view({'get': 'list'})(
            request,
            pk=self.vendor.pk
            )
        self.assertEqual(response.status_code, 200)
    
    def test_PurchaseOrderUpdateAPI(self):
        request = self.factory.patch(
            f'api/purchase_orders/{self.po.pk}',
            data={
                'po_number': '11222'
            },
            content_type='application/json')
        force_authenticate(request, user=self.vendor)
        response = PurchaseOrderViewSet.as_view({'patch': 'partial_update'})(
            request,
            pk=self.po.pk
            )
        self.assertEqual(response.status_code, 200)
    
    def test_PurchaseOrderCreateAPI(self):
        request = self.factory.post(
            f'api/purchase_orders/',
            data={
                'po_number': '12345aa89',
                'vendor': self.vendor.id,
                'estimated_delivery_date':dt.date.today()+dt.timedelta(days=5),
                'items': {'box': 'a large box'},
                'quantity': 10,
            },
            content_type='application/json')
        force_authenticate(request, user=self.vendor)
        response = PurchaseOrderViewSet.as_view({'post': 'create'})(
            request,
            )
        self.assertEqual(response.status_code, 201)
    
    def test_PurchaseOrderDeleteAPI(self):
        request = self.factory.delete(f'api/purchase_orders/{self.po.pk}')
        force_authenticate(request, user=self.vendor)
        response = PurchaseOrderViewSet.as_view({'delete': 'destroy'})(
            request,
            pk=self.po.pk
            )
        self.assertEqual(response.status_code, 204)
