# Generated by Django 4.0.3 on 2022-04-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceBill',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=1000)),
                ('product_type', models.CharField(max_length=1000)),
                ('gst_percentage', models.IntegerField()),
            ],
        ),
    ]
