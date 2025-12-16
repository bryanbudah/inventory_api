from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.InventoryItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', views.InventoryItemDetail.as_view(), name='item-detail'),
    path('report/', views.InventoryReport.as_view(), name='inventory-report'),

]
