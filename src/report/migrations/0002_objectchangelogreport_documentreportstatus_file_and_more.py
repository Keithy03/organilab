# Generated by Django 4.0.8 on 2023-07-04 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0122_create_base_unit_values'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectChangeLogReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laboratory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratory.laboratory')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratory.object')),
                ('task_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.taskreport')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratory.catalog')),
            ],
        ),
        migrations.AddField(
            model_name='documentreportstatus',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='reports/'),
        ),
        migrations.CreateModel(
            name='ObjectChangeLogReportBuilder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField()),
                ('new_value', models.FloatField(default=0.0)),
                ('old_value', models.FloatField(default=0.0)),
                ('diff_value', models.FloatField(default=0.0)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.objectchangelogreport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
