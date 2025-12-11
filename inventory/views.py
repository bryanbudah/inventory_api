from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from .models import InventoryItem
from .serializers import InventoryItemSerializer

def home(request):
    return HttpResponse("<h1>Welcome to Inventory API</h1><p>Go to /api/items/ to see inventory.</p>")

# List all items and create new item
class InventoryItemList(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]  # only authenticated users can create

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Retrieve, update, delete a single item
class InventoryItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
