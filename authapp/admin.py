from django.contrib import admin

from authapp.models import ShopUser
from ordersapp.models import Order

admin.site.register(ShopUser)
# admin.site.register(Order) # Order is already registered in app 'ordersapp'.

# @admin.register(Order)
# class PersonalAdmin(admin.ModelAdmin):
#     list_display = ('user', 'created', 'status')
#     list_filter = ('created', 'user')
# @admin.register(ShopUser)
# class PersonalAdmin(admin.ModelAdmin):
#     list_display = ('name', 'age')
#     # list_filter = ('created', 'name')

