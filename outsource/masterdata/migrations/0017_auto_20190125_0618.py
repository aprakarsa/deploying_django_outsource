# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-24 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0016_auto_20190123_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pub_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productpo',
            name='qty_invoice',
            field=models.IntegerField(default=0),
        ),
    ]