from django.contrib import admin
from django.utils.html import format_html


# Register your models here.
from .models import ItemDetail, CustomerDetail , OrderDetail , OrderItemDetail

class ItemDetailAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'price', 'category', 'status', 'image_tag')

admin.site.register(ItemDetail,ItemDetailAdmin)
admin.site.register(OrderDetail)
admin.site.register(OrderItemDetail)
admin.site.register(CustomerDetail)
