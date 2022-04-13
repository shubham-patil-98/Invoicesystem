from django.db import models

# Create your models here.
class InvoiceBill(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=1000)
    product_type=models.CharField(max_length=1000)
    gst_percentage=models.IntegerField()

    def __str__(self):
        return self.product_name
    
