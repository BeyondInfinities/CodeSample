# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_app', '0003_auto_20171111_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingtrips',
            name='item_spend',
            field=models.IntegerField(),
        ),
    ]
