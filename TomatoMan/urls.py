
from django.contrib import admin
from django.urls import path
from TomatoMan.views import index_page
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_page),
    path('items/',include("Items.urls")),
]
