# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-03 05:37
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_auto_20180630_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedurerequiredobject',
            name='measurement_unit',
            field=models.CharField(choices=[('0', 'Meters'), ('1', 'Milimeters'), ('2', 'Centimeters'), ('3', 'Liters'), ('4', 'Mililiters'), ('5', 'Unit'), ('6', 'Gram'), ('7', 'Kilogram'), ('8', 'Miligram'), ('9', 'Cubic Meter')], max_length=2, verbose_name='Measurement unit'),
        ),
    ]
