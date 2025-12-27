from django.http import HttpResponse
from rest_framework import generics, permissions
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, F
from .models import InventoryItem
from django.shortcuts import render


# -----------------------------
# Home View
# -----------------------------
def home(request):
    return HttpResponse(
        "<h1>Welcome to Inventory API</h1>"
        "<p>Go to <code>/api/items/</code> to see inventory.</p>"
    )


# -----------------------------
# List & Create Inventory Items
# -----------------------------
class InventoryItemList(generics.ListCreateAPIView):
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return only items owned by the logged-in user
        with optional filtering.
        """
        queryset = InventoryItem.objects.filter(owner=self.request.user)

        category = self.request.query_params.get('category')
        low_stock = self.request.query_params.get('low_stock')

        if category:
            queryset = queryset.filter(category__icontains=category)

        if low_stock == 'true':
            queryset = queryset.filter(quantity__lt=10)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# -----------------------------
# Retrieve, Update & Delete Item
# -----------------------------
class InventoryItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ensure users can only access their own items
        """
        return InventoryItem.objects.filter(owner=self.request.user)
    
class InventoryReport(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = InventoryItem.objects.filter(owner=request.user)

        total_items = items.count()
        total_quantity = items.aggregate(
            total=Sum('quantity')
        )['total'] or 0

        total_value = items.aggregate(
            value=Sum(F('quantity') * F('price'))
        )['value'] or 0

        return Response({
            "total_items": total_items,
            "total_quantity": total_quantity,
            "total_inventory_value": total_value
        })
    from django.shortcuts import render

def inventory_test_view(request):
    return render(request, 'inventory_test.html')

