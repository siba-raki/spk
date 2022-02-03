import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib import messages

from api.models import Product


from .models import Customer, SaleOrder, SaleOrderLine

from .froms import FormSaleOrder, FormSaleOrderLine



# Create your views here.
class CustomerView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            customers = list(Customer.objects.filter(id=id).values())
            if len(customers) > 0:
                customers = customers[0]
                datos = {"message":"Success", 'customers':customers}
            else:
                datos = {"message":"customers not found..."}
            return JsonResponse(datos)
        else:
            customers = list(Customer.objects.values())
            if len(customers)>0:
                datos = {"message":"Success", 'customers':customers}
            else:
                datos = {"message":"customers not found..."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Customer.objects.create(name=jd['name'], comment=jd['comment'])
        datos = {"message":"Success"}

        return JsonResponse(datos)

    def put(self, request, id):

        jd = json.loads(request.body)
        customers = list(Customer.objects.filter(id=id).values())

        if len(customers)>0:
            customers = Customer.objects.get(id=id)
            customers.name = jd ['name']
            customers.comment = jd ['comment']
            customers.save()   
            datos = {"message":"Success"}
        else:
            datos = {"message":"Customer not found..."}
        return JsonResponse(datos)


    def delete(self, request, id):

        customers = list(Customer.objects.filter(id=id).values())
        
        if len(customers)>0:
            Customer.objects.filter(id=id).delete()
            datos = {"message":"Success"}
        else:
            datos = {"message":"Customer not found..."}
        return JsonResponse(datos)


class SaleOrderView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            saleorders = list(SaleOrder.objects.filter(id=id).values())
            if len(saleorders) > 0:
                saleorders = saleorders[0]
                datos = {"message":"Success", 'saleorders':saleorders}
            else:
                datos = {"message":"saleorders not found..."}
            return JsonResponse(datos)
        else:
            saleorders = list(SaleOrder.objects.values())
            if len(saleorders)>0:
                datos = {"message":"Success", 'saleorders':saleorders}
            else:
                datos = {"message":"saleorders not found..."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        SaleOrder.objects.create(customer_id=jd['customer_id'],
        comment=jd['comment'], date=jd['date'], total=jd['total'])
        
        datos = {"message":"Success"}

        return JsonResponse(datos)

    def put(self, request, id):

        jd = json.loads(request.body)
        saleorders = list(SaleOrder.objects.filter(id=id).values())

        if len(saleorders)>0:
            saleorders = SaleOrder.objects.get(id=id)
            saleorders.customer_id = jd ['customer_id']
            saleorders.comment = jd ['comment']
            saleorders.date = jd ['date']
            saleorders.total = jd ['total']
            saleorders.save()   
            datos = {"message":"Success"}
        else:
            datos = {"message":"SaleOrder not found..."}
        return JsonResponse(datos)


    def delete(self, request, id):

        saleorders = list(SaleOrder.objects.filter(id=id).values())
        
        if len(saleorders)>0:
            SaleOrder.objects.filter(id=id).delete()
            datos = {"message":"Success"}
        else:
            datos = {"message":"saleorders not found..."}
        return JsonResponse(datos)



class SaleOrderLineView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            saleordersline = list(SaleOrderLine.objects.filter(id=id).values())
            if len(saleordersline) > 0:
                saleordersline = saleordersline[0]
                datos = {"message":"Success", 'saleordersline':saleordersline}
            else:
                datos = {"message":" saleordersline not found..."}
            return JsonResponse(datos)
        else:
            saleordersline = list(SaleOrderLine.objects.values())
            if len(saleordersline)>0:
                datos = {"message":"Success", 'saleordersline':saleordersline}
            else:
                datos = {"message":"saleordersline not found..."}
            return JsonResponse(datos)

    def price_total(quantity, price):
        price_total = (quantity * price)
        print (price_total)
        return price_total
  
    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        SaleOrderLine.objects.create(sale_order_id = jd['sale_order_id'], product_id = jd['product_id'],
        quantity = jd['quantity'], price = jd ['price'],)
        
        datos = {"message":"Success"}

        return JsonResponse(datos)

    def put(self, request, id):

        jd = json.loads(request.body)
        saleordersline = list(SaleOrderLine.objects.filter(id=id).values())

        if len(saleordersline)>0:
            saleordersline = SaleOrderLine.objects.get(id=id)
            saleordersline.sale_order_id = jd ['sale_order_id']
            saleordersline.product_id = jd ['product_id']
            saleordersline.quantity = jd ['quantity']
            saleordersline.price = jd ['price']
            saleordersline.price_total = jd ['price_total']
            saleordersline.save()   
            datos = {"message":"Success"}
        else:
            datos = {"message":"saleordersline not found..."}
        return JsonResponse(datos)


    def delete(self, request, id):

        saleordersline = list(SaleOrder.objects.filter(id=id).values())
        
        if len(saleordersline)>0:
            SaleOrderLine.objects.filter(id=id).delete()
            datos = {"message":"Success"}
        else:
            datos = {"message":"saleordersline not found..."}
        return JsonResponse(datos)

    def ventas(self, request, product_id):
        quantity = list(SaleOrderLine.objects.filter(product_id=product_id))
        lista = sum([q.quantity for q in quantity])
        datos = {'cantidades':lista}
        return JsonResponse(datos)
    


def create_saleorder(request):
    customers_data = Customer.objects.all()
    if request.method == 'POST':
        form = FormSaleOrder(request.POST)

        if form.is_valid():
            sale_order = SaleOrder()
            sale_order.comment = form.cleaned_data['comment']
            sale_order.date = form.cleaned_data['date']
            sale_order.total = form.cleaned_data['total']
            sale_order.customer_id = form.cleaned_data['customer_id']
            sale_order.save()
            response = redirect('/api/list_saleorder/')
            return response  
    else:
        form = FormSaleOrder()

    return render(request, 'create_saleorder.html', {'form' : form, 'customers': customers_data})

def list_saleorder(request):
    saleorders_data = SaleOrder.objects.all()
    if request.method == 'POST':

        if 'add' in request.POST:
            response = redirect('/api/create_saleorder/')
            return response
        elif 'delete' in request.POST:
            id = request.POST['delete']
            SaleOrder.objects.filter(id=id).delete()
      
    return render(request, 'list_saleorder.html', {'saleorders': saleorders_data})



def create_saleorderline(request):
    saleorders_data = SaleOrder.objects.all()
    products_data = Product.objects.all()
    if request.method == 'POST':
        form = FormSaleOrderLine(request.POST)
        if form.is_valid():
            sale_order_line = SaleOrderLine()
            sale_order_line.sale_order_id = form.cleaned_data['sale_order_id']
            sale_order_line.product_id = form.cleaned_data['product_id']
            sale_order_line.quantity = form.cleaned_data['quantity']
            sale_order_line.price = form.cleaned_data['price']
            sale_order_line.price_total = form.cleaned_data['price'] * form.cleaned_data['quantity']
            sale_order_line.save()
            response = redirect('/api/list_saleorderline/')
            return response
    else:
        form = FormSaleOrderLine()

    return render(request, 'create_saleorderline.html', {'form' : form, 'saleorders':saleorders_data, 'products':products_data})

def list_saleorderline(request):
    saleordersline_data = SaleOrderLine.objects.all()
    if request.method == 'POST':
        
        if 'add' in request.POST:
            response = redirect('/api/create_saleorderline/')
            return response
        
        elif 'delete' in request.POST:
            id = request.POST['delete']
            if id:
                SaleOrderLine.objects.filter(id=id).delete()
            
    return render(request, 'list_saleorderline.html', {'saleordersline': saleordersline_data})