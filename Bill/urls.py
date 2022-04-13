from rest_framework import routers
from django.urls import path,include
from . import views

routers=routers.DefaultRouter()
routers.register(r'InvoiceBill',views.InvoiceBillViewset)

urlpatterns = [
    path('',include(routers.urls)),
    path('api_auth',include('rest_framework.urls',namespace='rest_framework')),
]
