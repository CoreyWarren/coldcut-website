# Generated by Django 4.0.5 on 2022-06-30 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0004_alter_order_item_options_alter_store_image_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store_image',
            options={'verbose_name_plural': 'Store Images'},
        ),
    ]
