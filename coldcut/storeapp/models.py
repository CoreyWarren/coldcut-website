from django.db import models
import datetime
import environ
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


env = environ.Env()
environ.Env.read_env()

# Create your models here.

class Store_Item(models.Model):
    id = models.AutoField(null = False, primary_key=True)
    product_name = models.CharField(max_length=42, default = "No title yet.")
    category = models.CharField(max_length=42, default = "No category yet.")
    thumbnail = models.ImageField(upload_to='store/product-thumbnails/', height_field=None, width_field=None, max_length=100)
    item_images = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000, default = "No description yet.")
    date_post = models.DateField(default=datetime.date.today)


class Store_Images(models.Model):
    parent_item = models.ForeignKey(Store_Item, default = None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/product-images/')
    