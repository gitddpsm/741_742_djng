# Generated by Django 3.2.5 on 2021-08-30 21:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0039_alter_shopuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 1, 21, 56, 34, 899348)),
        ),
    ]
