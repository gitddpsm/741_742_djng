
from django.core.management.base import BaseCommand
import json
import os

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']

            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        ShopUser.objects.create_superuser(
            'admin', 'django@geekshop.local', '1234', age=30)
'''
    for el in catalog:
        ProductCategory.objects.get_or_create(name=el['category'])      # Создадим новую категорию, если такой не было
        category = ProductCategory.objects.filter(name=el['category'])  # Найдем эту категорию для получения ID
        product = Product(name=el['name'], category_id=category.values()[0]['id'], short_desc=el['short_desc'], image='products_images/'+el['image'], description=el['description'], price=el['price'], quantity=el['quantity'])
        product.save()
'''