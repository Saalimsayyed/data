# Generated by Django 4.2.4 on 2023-08-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_remove_purchase_item_remove_purchase_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='back',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='given',
            field=models.PositiveIntegerField(),
        ),
    ]
