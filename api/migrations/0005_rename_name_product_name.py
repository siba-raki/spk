# Generated by Django 4.0.2 on 2022-02-02 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_saleorder_customer_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Name',
            new_name='name',
        ),
    ]
