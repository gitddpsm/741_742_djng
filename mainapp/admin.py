from django.contrib import admin

from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)
# admin.site.register(Product)

@admin.register(Product)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    # list_filter = ('created', 'user')
# 