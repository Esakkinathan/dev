# Generated by Django 4.2.2 on 2023-06-29 06:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=40, verbose_name='id')),
                ('pasword', models.CharField(max_length=40, verbose_name='pasword')),
            ],
        ),
        migrations.CreateModel(
            name='Customer1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateField()),
                ('company', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('owner', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('weight', models.FloatField()),
                ('shipment', models.CharField(max_length=255)),
                ('trackingId', models.CharField(max_length=255)),
                ('shipmentSize', models.CharField(max_length=20)),
                ('boxCount', models.IntegerField()),
                ('specification', models.CharField(max_length=255)),
                ('checklistQuantity', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateField()),
                ('company', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('owner', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('weight', models.FloatField()),
                ('shipment', models.CharField(max_length=255)),
                ('trackingId', models.CharField(max_length=255)),
                ('shipmentSize', models.CharField(max_length=20)),
                ('boxCount', models.IntegerField()),
                ('specification', models.CharField(max_length=255)),
                ('checklistQuantity', models.CharField(max_length=255)),
            ],
        ),
    ]
