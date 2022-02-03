from django.db import models


# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    comment = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
       return str(self.id)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    comment = models.CharField(max_length=250, null=False, blank=False)
    def __str__(self) -> str:
    
        return str(self.id)

class SaleOrder(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete= models.CASCADE)
    comment = models.CharField(max_length=200, blank=False, null=False)
    date = models.DateTimeField(blank=False, null=False)
    total = models.BigIntegerField()

    def __str__(self):
       return str(self.id)

class SaleOrderLine(models.Model):
    id =models.AutoField(primary_key=True)
    sale_order_id = models.ForeignKey(SaleOrder, on_delete= models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.BigIntegerField()
    price = models.BigIntegerField()
    price_total = models.BigIntegerField()
    def __str__(self):
       return str(self.id)

    

    

