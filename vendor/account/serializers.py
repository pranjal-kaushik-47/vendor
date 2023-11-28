from rest_framework import serializers
from account.models import Vendor

class VendorSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('username')
        data.pop('password')
        return data
    
    class Meta:
        model = Vendor
        fields = "__all__"
