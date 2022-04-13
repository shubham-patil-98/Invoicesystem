from rest_framework import viewsets
from .models import InvoiceBill
from .mypagination import MyPageNumberPagination
from .serializers import InvoiceSerializer

# Create your views here.

class InvoiceBillViewset(viewsets.ModelViewSet):
    queryset=InvoiceBill.objects.all().order_by('product_name')
    pagination_class=MyPageNumberPagination
    serializer_class=InvoiceSerializer
