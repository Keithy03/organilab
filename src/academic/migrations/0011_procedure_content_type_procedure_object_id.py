# Generated by Django 4.0.8 on 2022-12-17 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('academic', '0010_update_sequences'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedure',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='procedure',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
