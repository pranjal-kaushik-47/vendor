from django.db import models
from account.models import Vendor

class OrderStatus(models.TextChoices):
    pending = 'Pending'
    completed = 'Completed'
    cancelled = 'Cancelled'

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=10, unique=True)
    vendor = models.ForeignKey(Vendor, related_name='orders', on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    estimated_delivery_date = models.DateField(null=True, blank=True)
    actual_delivery_date = models.DateField(null=True, blank=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(choices=OrderStatus.choices, max_length=20, default=OrderStatus.pending)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    acknowledgment_date = models.DateField(null=True, blank=True)