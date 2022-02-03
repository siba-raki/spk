from django import forms
from django.db import models
from django.forms.widgets import NumberInput
from datetime import date

from .models import Customer, SaleOrder, SaleOrderLine, Product


class FormCustomer(forms.Form):
    """Formulario de Reistro de un cliente
    variables = 
    Nombre :
    Comment:
    """
    name = forms.CharField(label='Nombre',max_length=50, required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea(attrs={'row':5, 'cols':20 }))
    
class FormSaleOrder(forms.Form):
    customer_id = forms.ModelChoiceField(label='id cliente', queryset=Customer.objects.all(), initial = 0)
    total = forms.IntegerField()
    date = forms.DateTimeField(initial=date.today, widget=NumberInput(attrs={'type': 'date'}))
    comment= forms.CharField(max_length=200)

class FormSaleOrderLine(forms.Form):
    sale_order_id = forms.ModelChoiceField(label='id order', queryset=SaleOrder.objects.all(),initial = 0)
    product_id = forms.ModelChoiceField(label='id producto', queryset=Product.objects.all(), initial = 0)
    quantity = forms.IntegerField()
    price= forms.IntegerField()