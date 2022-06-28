# Generated by Django 4.0.5 on 2022-06-28 08:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store_Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='No title yet.', max_length=42)),
                ('category', models.CharField(default='No category yet.', max_length=42)),
                ('thumbnail', models.ImageField(upload_to='store/product-thumbnails/')),
                ('description', models.CharField(default='No description yet.', max_length=2000)),
                ('date_post', models.DateField(default=datetime.date.today)),
                ('item_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='store/product-images/')),
                ('parent_item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='storeapp.store_item')),
            ],
        ),
    ]