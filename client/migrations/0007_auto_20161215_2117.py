# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 21:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20161215_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Fecha y hora de transaccion'),
        ),
    ]