# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 23:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_transaction', models.IntegerField(verbose_name=b'Numero de transaccion')),
                ('fecha', models.DateField(verbose_name=b'Fecha y hora de transaccion')),
                ('concepto', models.CharField(max_length=200, verbose_name=b'Concepto')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente2', to='client.Client')),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente1', to='client.Client')),
            ],
        ),
    ]