# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-22 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0012_remove_product_barcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('invoice_no', models.CharField(max_length=15, unique=True)),
                ('po_customer', models.CharField(max_length=50)),
            ],
        ),
    ]