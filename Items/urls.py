from django.urls import path
from . import views
from django.conf import settings



urlpatterns = [
path('', views.index),
 path('address/', views.add_address),
path('items/',views.item_api),
path('items/<str:pk>/',views.item_detail_api),
path('customer/',views.customer_address_api_post),
path('address_api/mobile/',views.address_details_viaMob),
path('order_api/mobile/',views.order_details_viaMob),
path('place_order/',views.place_order),

]
