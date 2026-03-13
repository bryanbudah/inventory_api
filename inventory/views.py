from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, F

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import InventoryItem
from .serializers import InventoryItemSerializer

# -----------------------------
# Inventory Test Page
# -----------------------------
def inventory_test_view(request):
    return render(request, 'inventory_test.html')

# -----------------------------
# Inventory API
# -----------------------------
@method_decorator(csrf_exempt, name='dispatch')
class InventoryItemList(generics.ListCreateAPIView):
    serializer_class = InventoryItemSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = InventoryItem.objects.all()
        category = self.request.query_params.get('category')
        low_stock = self.request.query_params.get('low_stock')

        if category:
            queryset = queryset.filter(category__icontains=category)
        if low_stock == 'true':
            queryset = queryset.filter(quantity__lt=10)
        return queryset

    def perform_create(self, serializer):
        serializer.save()

@method_decorator(csrf_exempt, name='dispatch')
class InventoryItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InventoryItemSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return InventoryItem.objects.all()

@method_decorator(csrf_exempt, name='dispatch')
class InventoryReport(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = InventoryItem.objects.all()
        total_items = items.count()
        total_quantity = items.aggregate(total=Sum('quantity'))['total'] or 0
        total_value = items.aggregate(value=Sum(F('quantity') * F('price')))['value'] or 0
        return Response({
            "total_items": total_items,
            "total_quantity": total_quantity,
            "total_inventory_value": total_value
        })

