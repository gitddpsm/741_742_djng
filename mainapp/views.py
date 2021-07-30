from django.shortcuts import render

from mainapp.models import Product


def index(request):
<<<<<<< HEAD
    title = 'кателог'
=======
    title = 'каталог'
>>>>>>> 1949e04c3255be960f0905b08038d68a461762f4

    links_menu = [
        {'href': 'index', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    products = Product.objects.all()[:4]

    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': products,
    }
    return render(request, 'mainapp/products.html', context)
