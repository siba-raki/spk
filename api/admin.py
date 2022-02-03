from django.contrib import admin
from .models import Product, Customer, SaleOrder, SaleOrderLine


# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(SaleOrder)
admin.site.register(SaleOrderLine)