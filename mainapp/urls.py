from django.urls import path
from .views import products, product

app_name = 'mainapp'

urlpatterns = [
    # path('', products, name='index'),
    path('', products, name='index'),
    # path('category/<int:pk>/', mainapp.products, name='category'),
    path('category/<int:pk>/', products, name='category'),
    # path('product/<int:pk>/', product, name='product'),
]
