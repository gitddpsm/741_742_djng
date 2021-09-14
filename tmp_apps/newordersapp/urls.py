import newordersapp.views as nordersapp
from django.urls import re_path

app_name="newordersapp"

urlpatterns = [
   re_path(r'^$', nordersapp.OrderList.as_view(), name='orders_list'),
   re_path(r'^forming/complete/(?P<pk>\d+)/$',
           nordersapp.order_forming_complete, name='order_forming_complete'),
   re_path(r'^create/$', nordersapp.OrderItemsCreate.as_view(),
           name='order_create'),
   re_path(r'^read/(?P<pk>\d+)/$', nordersapp.OrderRead.as_view(),
           name='order_read'),
   re_path(r'^update/(?P<pk>\d+)/$', nordersapp.OrderItemsUpdate.as_view(),
           name='order_update'),
   re_path(r'^delete/(?P<pk>\d+)/$', nordersapp.OrderDelete.as_view(),
           name='order_delete'),
]