from django.urls import path
from adminapp.views import (
    # users,
    # user_create,
    user_update,
    product_update,
    user_delete,
    # category_create,
    categories,
    # category_delete,
    category_update,
    products,
    # product_read,
    product_create,
    product_delete, 
    UserListView, 
    UserCreateView, 
    ProductDetailView,
    ProductCategoryDelete,
    ProductCategoryAble,
    ProductCategoryCreate,
    ProductCategoryUpdate,
)
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.UserCreateView.as_view(), name='user_create'),
    path('users/read/', adminapp.UserListView.as_view(), name='users'),
    path('users/update/<int:pk>/', user_update, name='user_update'),
    path('users/delete/<int:pk>/', user_delete, name='user_delete'),

    # path('categories/create/', category_create, name='category_create'),
    path('categories/create/', adminapp.ProductCategoryCreate.as_view(), name='category_create'),
    path('categories/read/', categories, name='categories'),
    # path('categories/update/<int:pk>/', adminapp.ProductCategoryUpdate.as_view(), name='category_update'),
    path('categories/update/<int:pk>/', category_update, name='category_update'),
    # path('categories/delete/<int:pk>/', category_delete, name='category_delete'),
    
    path('categories/delete/<int:pk>/', adminapp.ProductCategoryDelete.as_view(), name='category_delete'),
    path('categories/able/<int:pk>/', adminapp.ProductCategoryAble.as_view(), name='category_able'),

    path('products/create/category/<int:pk>/', product_create, name='product_create'),
    path('products/read/category/<int:pk>/', products, name='products'),
    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    # path('products/read/<int:pk>/', product_read, name='product_read'),
    path('products/update/<int:pk>/', product_update, name='product_update'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),
]