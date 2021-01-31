from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from Items.models import CustomerDetails , ItemDetails  , OrderItemDetails,OrderDetails
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .serializers import ItemSerializer , CustomerSerializer , OrderSerializer , OrderItemSerializer
#   , LoginSerializer , OrderSerializer

def index(request):
    return HttpResponse("Items Page")

def add_address(request):
    return render(request, 'Items/address.html')

# def cust_address(request):
#     fullname = request.POST['fullname']
#     mobile = request.POST['mobile']
#     pincode = request.POST['pincode']
#     address = request.POST['address']
#     city = request.POST['city']

# # def detail(request, item_id):
# #     item = get_object_or_404(ItemDetails,pk=item_id)
# #     context = {'item': item}
# #     return render(request, 'Item/image_view.html', context)


#     customeraddress = CustomerDetails(fullname=fullname, mobile=mobile, pincode=pincode,
#     address=address, city = city)
    # message = ""

    # try:
    #     customeraddress.save()
    #     message = "Customer data submitted."
    # except:
    #     message = ("Can't save Customer details. try again")

    # context = {'message':message}
    # return render(request, 'Items/address.html', context)

# def display_images(request): 
  
#     if request.method == 'GET': 
#         # getting all the objects of hotel. 
#         item = ItemDetails.objects.all()  
#         return render(request, 'Items/image_view.html', {'item_images' : item})


@csrf_exempt
def item_api(request):
    if request.method == 'GET':
        items = ItemDetails.objects.all()
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
        items = ItemDetails.objects.get(pk=pk)
    except ItemDetails.DoesNotExist:
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
def customer_address_api_get(request,pk):
    # if request.method == 'GET':
    #     address = CustomerDetails.objects.get(pk=pk)
    #     serializer = CustomerSerializer(address,many=True)
    #     return JsonResponse(serializer.data,safe=False)
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = CustomerSerializer(data=data)

    try:
        address = CustomerDetails.objects.get(pk=pk)
    except CustomerDetails.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CustomerSerializer(address)
        return JsonResponse(serializer.data)
    
    
   

@csrf_exempt
def customer_address_api_post(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        
        obj , created = CustomerDetails.objects.update_or_create(mobile=data['mobile'],
        defaults={"fullname": data['fullname'],"address":data['address'],"landmark":data['landmark']})
        get_name = data["mobile"]
        value = CustomerDetails.objects.filter(mobile=get_name)
        serializer = CustomerSerializer(value, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    return JsonResponse(serializer2.errors,status=400)

        
        # return JsonResponse("neither creted nor updated",status=400)
    


from django.utils import timezone
@csrf_exempt
def address_details_viaMob(request):
    if request.method == 'POST':
       print(request.body)
       data = JSONParser().parse(request)
       get_name = data["mobile"]
       value = CustomerDetails.objects.filter(mobile=get_name)
       serializer = CustomerSerializer(value, many=True)
       return JsonResponse(serializer.data, safe=False,status=200)
    return JsonResponse(serializer.errors, safe=False,status=400)

# @csrf_exempt
# def login_details(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = CustomerSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#             return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def order_details_viaMob(request):
    if request.method == 'POST':
       print(request.body)
       data = JSONParser().parse(request)
       get_name = data["customer_id"]
       value = OrderDetails.objects.filter(customer_id=get_name)
       serializer = OrderSerializer(value, many=True) 
       return JsonResponse(serializer.data, safe=False,status=200)
    return JsonResponse(serializer.errors, safe=False,status = 400)


import json
@csrf_exempt
def place_order(request):
    # if request.method == 'GET':
    #     order = OrderItemDetails.objects.all()
    #     serializer2 = OrderItemSerializer(order,many=True)
    #     return JsonResponse(serializer2.data,safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        order_data = data.get('order')
        serializer1 = OrderSerializer(data=order_data)
    
        if serializer1.is_valid():
            serializer1.save()
            
            var_order_id = serializer1["id"]
            print("order id ",var_order_id.value)
            # getArray = json.load(items)
            items = data['items']
            print(len(items))
            for item in items:
                print("hello")
                item['order'] = var_order_id.value
                serializer2 =OrderItemSerializer(data = item)
                if serializer2.is_valid():
                    serializer2.save()
                
            return JsonResponse(serializer2.errors,status=400)
            return JsonResponse(serializer1.data,status=200)
        return JsonResponse(serializer1.errors,status=400)

    # if request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer2 = OrderItemSerializer(data=data)
    
    #     if serializer2.is_valid():
    #         serializer2.save()
    #         return JsonResponse(serializer2.data,status=201)
    #         return JsonResponse(serializer2.errors,status=400)

