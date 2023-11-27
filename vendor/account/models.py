from django.db import models
from django.contrib.auth.models import AbstractUser


class Vendor(AbstractUser):
    name = models.CharField(max_length=100, default='vendor')
    contact_details = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    vendor_code = models.CharField(max_length=10, unique=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='performance', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)