# dd
import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def get_basket(user):
#     if user.is_authenticated:
#         return Basket.objects.filter(user=user)
#     else:
#         return []


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def products(request, pk=None, page = 1):
    title = 'продукты'
    # same_products = Product.objects.all()[:3]
    # basket = get_basket(request.user)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    links_menu = ProductCategory.objects.all()
    products = Product.objects.all().order_by('price')

    if pk is not None:
        if pk == 0:
            products = Product.objects.filter(is_active = True).order_by('price')
            # products = Product.objects.all().order_by('price')
            category = {'pk': 0, 'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(is_active = True, category__pk = pk).order_by('price')
            # products = Product.objects.filter(category__pk=pk).order_by('price')

        paginator = Paginator(products, 3)

        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)


        context = {
            'title': title,
            'links_menu': links_menu,
            'hot_product': hot_product,
            # 'related_products': same_products,
            'same_products': same_products,
            'products': products_paginator,
            # 'basket': basket,
            'category': category,
        }
        return render(request=request, template_name='mainapp/products.html', context=context)

    # same_products = Product.objects.all()[:3]
    # products = Product.objects.all().order_by('price')

    context = {
        'title': title,
        'links_menu': links_menu,
        # 'related_products': same_products,
        'hot_product': hot_product,
        'same_products': same_products,
        'products': products,
        # 'basket': basket,
    }

    return render(request = request, template_name = 'mainapp/products.html', context = context)


def product(request, pk):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    # basket = get_basket(request.user)

    product = get_object_or_404(Product, pk=pk)

    same_products = get_same_products(product)
    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': same_products,
        # 'basket': basket,
        'product': product,
    }
    return render(request, 'mainapp/product.html', context)
    