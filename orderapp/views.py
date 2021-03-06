from .models import Order
from .serializers import OrderSerializer
from rest_framework import viewsets


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-cost')
    serializer_class = OrderSerializer
