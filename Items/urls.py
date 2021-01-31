from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('', views.index),
 path('address/', views.add_address),
# path('cust_address/', views.cust_address),
# path('item_images',views.display_images, name = 'item_images'),
path('items/',views.item_api),
path('items/<str:pk>/',views.item_detail_api),
path('customer/',views.customer_address_api_post),
path('customer_api/customer/<int:pk>/',views.customer_address_api_get),
# path('order_api/checkout/',views.order_details),
path('address_api/mobile/',views.address_details_viaMob),
path('order_api/mobile/',views.order_details_viaMob),
path('place_order/',views.place_order),

# path('login/',views.login_details),



# path('<int:item_id>/', views.detail,name='detail'),

]
# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


