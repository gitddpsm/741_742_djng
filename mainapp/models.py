from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_lenght=64, unique=True)
