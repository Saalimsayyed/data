# Generated by Django 4.2.4 on 2023-08-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_back_alter_product_given'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feet',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
