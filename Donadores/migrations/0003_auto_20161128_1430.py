# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donadores', '0002_auto_20161122_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donaciones_monetarias',
            name='Cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
