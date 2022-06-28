from django.contrib import admin

from storeapp.models import Store_Images, Store_Item

# Register your models here.
admin.site.register(Store_Item)
admin.site.register(Store_Images)