from django.db.models.signals import post_save, pre_save
from purchase_management.models import PurchaseOrder, OrderStatus
from account.models import HistoricalPerformance, Vendor
from django.dispatch import receiver
import datetime as dt
from django.db.models import Avg, F


@receiver(pre_save, sender=PurchaseOrder)
def handel_oldinstance(sender, instance, **kwargs):
    old_instance = PurchaseOrder.objects.filter(id=instance.id).last()
    instance.old_instance = old_instance


@receiver(post_save, sender=PurchaseOrder)
def handel_orders(sender, instance, created, **kwargs):
    if not created:
        orders = PurchaseOrder.objects.filter(vendor_id=instance.vendor_id)
        on_time_delivery_rate = quality_rating_avg = average_response_time = fulfillment_rate = None
        if instance.old_instance.status != OrderStatus.completed and instance.status == OrderStatus.completed:
            on_time_delivery_rate = orders.filter(actual_delivery_date__lte=F('estimated_delivery_date')).count()/orders.count() if orders.count() else None
            if instance.quality_rating:
                quality_rating_avg = orders.filter(quality_rating__isnull=False).aggregate(Avg('quality_rating')).get('quality_rating__avg')
        if instance.acknowledgment_date != instance.old_instance.acknowledgment_date:
            average_response_time = orders.annotate(resp=F('acknowledgment_date')-F('issue_date')).aggregate(Avg('resp')).get('resp__avg')
        if instance.old_instance.status != instance.status:
            fulfillment_rate = orders.filter(status=OrderStatus.completed).count()/orders.count() if orders.count() else None
        
        historical_performance, created = HistoricalPerformance.objects.get_or_create(
            vendor_id=instance.vendor_id,
            date=dt.date.today()
        )
        if on_time_delivery_rate:
            historical_performance.on_time_delivery_rate = on_time_delivery_rate
        if quality_rating_avg:
            historical_performance.quality_rating_avg = quality_rating_avg
        if average_response_time:
            historical_performance.average_response_time = average_response_time.total_seconds()/60
        if fulfillment_rate:
            historical_performance.fulfillment_rate = fulfillment_rate
        historical_performance.save()

        vendor = Vendor.objects.get(id=instance.vendor_id)
        vendor.on_time_delivery_rate = HistoricalPerformance.objects.filter(vendor_id=instance.vendor_id).aggregate(Avg('on_time_delivery_rate')).get('on_time_delivery_rate__avg')
        vendor.quality_rating_avg = HistoricalPerformance.objects.filter(vendor_id=instance.vendor_id).aggregate(Avg('quality_rating_avg')).get('quality_rating_avg__avg')
        vendor.average_response_time = HistoricalPerformance.objects.filter(vendor_id=instance.vendor_id).aggregate(Avg('average_response_time')).get('average_response_time__avg')
        vendor.fulfillment_rate = HistoricalPerformance.objects.filter(vendor_id=instance.vendor_id).aggregate(Avg('fulfillment_rate')).get('fulfillment_rate__avg')
        vendor.save()

        
