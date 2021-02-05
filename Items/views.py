from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from Items.models import CustomerDetail , ItemDetail  , OrderItemDetail,OrderDetail
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .serializers import ItemSerializer , CustomerSerializer , OrderSerializer , OrderItemSerializer

def index(request):
    return HttpResponse("Items Page")

def add_address(request):
    return render(request, 'Items/address.html')


@csrf_exempt
def item_api(request):
    if request.method == 'GET':
        items = ItemDetail.objects.all()
        serializer = ItemSerializer(items,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status=201)
    return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def item_detail_api(request,pk):
    try:
        items = ItemDetail.objects.get(pk=pk)
    except ItemDetail.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ItemSerializer(items)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(items,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse("Item deleted")

@csrf_exempt
def customer_address_api_post(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        
        obj , created = CustomerDetail.objects.update_or_create(mobile=data['mobile'],
        defaults={"fullname": data['fullname'],"address":data['address'],"landmark":data['landmark']})
        get_name = data["mobile"]
        value = CustomerDetail.objects.filter(mobile=get_name)
        serializer = CustomerSerializer(value, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    return JsonResponse(serializer2.errors,status=400)
    


from django.utils import timezone
@csrf_exempt
def address_details_viaMob(request):
    if request.method == 'POST':
       print(request.body)
       data = JSONParser().parse(request)
       get_name = data["mobile"]
       value = CustomerDetail.objects.filter(mobile=get_name)
       serializer = CustomerSerializer(value, many=True)
       return JsonResponse(serializer.data, safe=False,status=200)
    return JsonResponse(serializer.errors, safe=False,status=400)

@csrf_exempt
def order_details_viaMob(request):
    if request.method == 'POST':
       print(request.body)
       data = JSONParser().parse(request)
       get_name = data["customer_id"]
       value = OrderDetail.objects.filter(customer_id=get_name)
       serializer = OrderSerializer(value, many=True) 
       return JsonResponse(serializer.data, safe=False,status=200)
    return JsonResponse(serializer.errors, safe=False,status = 400)


@csrf_exempt
def place_order(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        order_data = data.get('order')
        serializer1 = OrderSerializer(data=order_data)
    
        if serializer1.is_valid():
            serializer1.save()
            
            var_order_id = serializer1["id"]
            print("order id ",var_order_id.value)
            items = data['items']
            print(len(items))
            save_data = True
            for item in items:
                print("hello")
                item['order'] = var_order_id.value
                serializer2 =OrderItemSerializer(data = item)
                if serializer2.is_valid():
                    serializer2.save()
                else:
                    save_data = False
            if save_data == False:
                return JsonResponse(serializer2.errors,status=400)
            return JsonResponse(serializer1.data,status=200)
        return JsonResponse(serializer1.errors,status=400)
