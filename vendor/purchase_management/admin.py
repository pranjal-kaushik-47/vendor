from django.contrib import admin
from purchase_management.models import PurchaseOrder


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = (
        "po_number",
        "vendor",
        "order_date",
        "estimated_delivery_date",
        "actual_delivery_date",
        "items",
        "quantity",
        "status",
        "quality_rating",
        "issue_date",
        "acknowledgment_date"
    )