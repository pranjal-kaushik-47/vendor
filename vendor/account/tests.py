from django.test import TestCase, RequestFactory
from rest_framework.test import force_authenticate
from .views import (
    VendorViewSet
)
from .models import (
    Vendor
)


class TestApi(TestCase):
    def setUp(self) -> None:
        self.vendor = Vendor.objects.create(
            name='vendor1',
            contact_details='123',
            address='address',
            vendor_code='123'
        )
        self.factory = RequestFactory()

    def test_VendorListAPI(self):
        request = self.factory.get(
            'api/vendors/')
        force_authenticate(request, user=self.vendor)
        response = VendorViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
    
    def test_VendorGetAPI(self):
        request = self.factory.get(
            'api/vendors/')
        force_authenticate(request, user=self.vendor)
        response = VendorViewSet.as_view({'get': 'list'})(
            request,
            pk=self.vendor.pk
            )
        self.assertEqual(response.status_code, 200)
    
    def test_VendorUpdateAPI(self):
        request = self.factory.patch(
            f'api/vendors/{self.vendor.pk}',
            data={
                'name': 'vendor2'
            },
            content_type='application/json')
        force_authenticate(request, user=self.vendor)
        response = VendorViewSet.as_view({'patch': 'partial_update'})(
            request,
            pk=self.vendor.pk
            )
        self.assertEqual(response.status_code, 200)
    
    def test_VendorCreateAPI(self):
        request = self.factory.post(
            f'api/vendors/',
            data={
                'name': 'vendor3',
                'contact_details': '123',
                'address':'address',
                'vendor_code': '123**',
                'username': 'vendor3',
                'password': 'pass'
            },
            content_type='application/json')
        force_authenticate(request, user=self.vendor)
        response = VendorViewSet.as_view({'post': 'create'})(
            request,
            )
        self.assertEqual(response.status_code, 201)
    
    def test_VendorDeleteAPI(self):
        request = self.factory.delete(f'api/vendors/{self.vendor.pk}')
        force_authenticate(request, user=self.vendor)
        response = VendorViewSet.as_view({'delete': 'destroy'})(
            request,
            pk=self.vendor.pk
            )
        self.assertEqual(response.status_code, 204)
