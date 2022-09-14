# Generated by Django 3.2 on 2022-09-12 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('status', models.CharField(choices=[('admin', 'Creating form'), ('fill', 'Filling form'), ('result', 'Form results')], max_length=6)),
                ('schema', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='CustomFormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('label', models.CharField(max_length=40)),
                ('label_suffix', models.CharField(blank=True, max_length=10, null=True)),
                ('help_text', models.CharField(blank=True, max_length=100, null=True)),
                ('initial', models.CharField(blank=True, max_length=40, null=True)),
                ('required', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
                ('localize', models.BooleanField(default=False)),
                ('props_css', models.CharField(blank=True, max_length=300, null=True)),
                ('extra_args', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FieldType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_name', models.CharField(max_length=80)),
                ('display_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='derb.customform')),
            ],
        ),
        migrations.CreateModel(
            name='WidgetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_name', models.CharField(max_length=80)),
                ('display_name', models.CharField(max_length=40)),
                ('extra_args', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Validator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('parameters', models.JSONField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='validators', to='derb.customformfield')),
            ],
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsections', to='derb.section')),
            ],
        ),
        migrations.AddField(
            model_name='customformfield',
            name='field_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='derb.fieldtype'),
        ),
        migrations.AddField(
            model_name='customformfield',
            name='subsection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='derb.subsection'),
        ),
        migrations.AddField(
            model_name='customformfield',
            name='widget_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='derb.widgettype'),
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.JSONField(blank=True, null=True)),
                ('conditional_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variable_fields', to='derb.customformfield')),
            ],
        ),
    ]
