from django.apps import AppConfig


class PurchaseManagementConfig(AppConfig):
    name = 'purchase_management'

    def ready(self) -> None:
        import purchase_management.signals
