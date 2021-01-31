from django.contrib import admin



# Register your models here.
from .models import ItemDetails, CustomerDetails , OrderDetails , OrderItemDetails


# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('name','image_preview')
#     readonly_fields = ('image_preview',)

#     def image_preview(self, obj):
#         return obj.image_preview

#     image_preview.short_description = 'Image Preview'
#     image_preview.allow_tags = True


admin.site.register(ItemDetails)
admin.site.register(OrderDetails)
admin.site.register(OrderItemDetails)
admin.site.register(CustomerDetails)
