from Items.models import ItemDetails , CustomerDetails , OrderDetails , OrderItemDetails
# ,LoginDetails,OrderDetails
from rest_framework import serializers
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetails
        fields = ['name', 'price', 'category','status','image']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = ['fullname','mobile',  'address' , 'landmark']

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomerDetails
#         fields = ['customer_details','name','price', 'date', 'quantity','order_status']


# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomerDetails
#         fields = ['customer_details', 'order_details' , 'date' , 'order_status' ]

# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LoginDetails
#         fields = ['mobile']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ['id','customer', 'date' , 'payment_mode' , 'payment_status', 'total_amount']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemDetails
        fields = ['order', 'item' , 'price' , 'quantity']
