# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0003_auto_20160809_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='shelf',
        ),
        migrations.AddField(
            model_name='shelfobject',
            name='shelf',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='laboratory.Shelf'),
            preserve_default=False,
        ),
    ]
