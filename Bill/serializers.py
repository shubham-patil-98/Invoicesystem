from rest_framework import serializers
from .models import InvoiceBill

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=InvoiceBill
        # fields=['product_id','product_name','product_type','gst_percentage']
        fields='__all__'