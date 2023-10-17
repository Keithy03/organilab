# Generated by Django 4.1.11 on 2023-10-17 17:18

from django.db import migrations, models
import risk_management.models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_management', '0008_auto_20230120_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentreport',
            name='notification_copy',
            field=models.FileField(blank=True, null=True, upload_to=risk_management.models.upload_notification_copy, verbose_name='En caso de intoxicación adjuntar copia de la notificación realizada al Centro Nacional de Control de Intoxicaciones (CNCI)'),
        ),
    ]
