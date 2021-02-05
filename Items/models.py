from django.db import models
from django.db.models import Model
from django.utils.safestring import mark_safe
from django.utils import timezone
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = 'photos/'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class ItemDetail(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=20, choices=[('Fruits', 'Fruits'), ('Vegetable', 'Vegetable')])
    status = models.CharField(max_length=20 ,choices=[(' ', ' In stock') , ('Out Of Stock', 'out of stock')])
    image = models.ImageField(upload_to=path_and_rename)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'
    
    def __str__(self):
        return ('Name: {name} Price: {price} Category: {category} Status: {status} Image: {image}' \
        .format(name = self.name, price= self.price , category= self.category,status= self.status, image = self.image))


class CustomerDetail(models.Model):
    fullname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12, primary_key=True)
    address = models.CharField(max_length=1000)
    landmark = models.CharField(max_length=500)
    

    def __str__(self):
        return (' Full Name: {fullname} Mobile No: {mobileno}  Address: {address} Landmark: {landmark} ' \
        .format( fullname = self.fullname, mobileno = self.mobile  ,address = self.address , landmark = self.landmark ))
    



class OrderDetail(models.Model):
    customer = models.ForeignKey(CustomerDetail, on_delete = models.CASCADE)
    date = models.DateTimeField('date published',default=timezone.now())
    payment_mode = models.CharField(max_length=100 ,choices=[('Pay On Delivery', 'Pay On Delivery') , ('UPI', 'UPI'),('Net Banking', 'Net Banking'),('Credit Card/Debit Card', 'Credit Card/Debit Card')],default='Pay On Delivery')
    payment_status = models.CharField(max_length=100 ,choices=[('Pending', 'Pending') , ('Received', 'Received')],default="Pending")
    total_amount = models.CharField(max_length=20)

    def __str__(self):
        return ('Customer: {customer} Date: {date} Payment Mode {payment_mode} Payment Status {payment_status} Total {total_amount}'
        .format(customer = self.customer , date = self.date , payment_mode = self.payment_mode , payment_status = self.payment_status , total_amount = self.total_amount) )



class OrderItemDetail(models.Model):
    order = models.ForeignKey(OrderDetail , on_delete = models.CASCADE)
    item = models.ForeignKey(ItemDetail , on_delete = models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return ('Order Details : {order} Ordered Item Details: {item} Price: {price} Quantity: {quantity} '
        .format(order= self.order , item = self.item , price  = self.price , quantity = self.quantity ))
































# class OrderDetails(models.Model):
#     customer_details = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
#     name = models.ForeignKey(ItemDetails,to_field='name', related_name='itemname' ,  on_delete=models.CASCADE)
#     price = models.ForeignKey(ItemDetails,to_field='price',related_name='itemprice' , on_delete=models.CASCADE)
#     date = models.DateTimeField('date published',default=timezone.now())
#     quantity = models.CharField(max_length=500)
#     order_status = models.CharField(max_length=20, choices=[('Received', 'Received'), ('Shipped', 'Shipped'),
#      ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')])

#     def __str__(self):
#         return (' Full Name: {customer_detials} Item Name: {name} price: {price} Date: {date} Quantity: {quantity} Order Status: {order_status}' \
#         .format( customer_details = self.customer_details, name = self.name , price= self.price, date = self.date ,quantity = self.quantity , order_status = self.order_status))
    

# class OrderDetails(models.Model):
#     customer_details = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
#     item_details = models.ForeignKey(ItemDetails, on_delete=models.CASCADE,default= "")
#     quantity = models.CharField(max_length=500)
#     # order_details = PickledObjectField()
#     date = models.DateTimeField('date published',default=timezone.now())
#     order_status = models.CharField(max_length=20, choices=[('Received', 'Received'), ('Shipped', 'Shipped'),
#      ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')] , default="Received" )

#     def __str__(self):
#         return (' Customer Details: {customer_detials} Order Details: {order_details} Date: {date}  Order Status: {order_status}' \
#         .format( customer_details = self.customer_details, order_details = self.order_details , date = self.date , order_status = self.order_status))
    

