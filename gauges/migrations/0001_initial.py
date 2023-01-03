# Generated by Django 4.1.5 on 2023-01-03 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gauge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True, verbose_name='Identification key')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kwh', models.PositiveIntegerField(verbose_name='kWh')),
                ('registered_at', models.DateTimeField(verbose_name='Registered at')),
                ('gauge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gauges.gauge', verbose_name='Gauge')),
            ],
        ),
    ]
