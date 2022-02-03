from django.urls import path
from api.views import *

urlpatterns = [
    path('customer/', CustomerView.as_view(), name = 'Customer_list'),
    path('customer/<int:id>', CustomerView.as_view(), name = 'customer_process'),

    path('saleorder/', SaleOrderView.as_view(), name = 'SaleOrder_list'),
    path('saleorder/<int:id>', SaleOrderView.as_view(), name = 'SaleOrder_proceess'),

    path('saleorderline/', SaleOrderLineView.as_view(), name = 'SaleOrderLine_list'),
    path('saleorderline/<int:id>', SaleOrderLineView.as_view(), name = 'SaleOrderLine_proceess'),

    path('create_saleorder/', create_saleorder, name = 'create_SaleOrder'),
    path('delete_saleorder/', delete_saleorder, name = 'delete_SaleOrder'),
    path('create_saleorderline/', create_saleorderline, name = 'create_SaleOrderLine'),
    path('delete_saleorderline/', delete_saleorderline, name = 'delete_SaleOrderLine'),

]  