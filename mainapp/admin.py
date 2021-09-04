from django.contrib import admin

from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)
admin.site.register(Product)

# @admin.register(Order)
# class PersonalAdmin(admin.ModelAdmin):
#     list_display = ('user', 'created', 'status')
#     list_filter = ('created', 'user')
# 