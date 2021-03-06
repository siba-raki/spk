# Generated by Django 4.0.1 on 2022-01-30 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SaleOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('total', models.BigIntegerField()),
                ('customer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
            ],
        ),
        migrations.CreateModel(
            name='SaleOrderLine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quatity', models.BigIntegerField()),
                ('price', models.BigIntegerField()),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('sale_order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.saleorder')),
            ],
        ),
    ]
