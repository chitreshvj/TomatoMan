from Items.models import ItemDetail , CustomerDetail , OrderDetail , OrderItemDetail
from rest_framework import serializers
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetail
        fields = ['name', 'price', 'category','status','image']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = ['fullname','mobile',  'address' , 'landmark']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['id','customer', 'date' , 'payment_mode' , 'payment_status', 'total_amount']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemDetail
        fields = ['order', 'item' , 'price' , 'quantity']
