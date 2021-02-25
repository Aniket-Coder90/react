from django.urls import path
from cafe.views import MenuList, OrderList

urlpatterns = [
    path('',MenuList.as_view(), name='menu'),
    path('checkout/',OrderList.as_view(), name='order'),
]
