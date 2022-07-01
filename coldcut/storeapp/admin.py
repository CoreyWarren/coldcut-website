from django.contrib import admin

from storeapp.models import Store_Image, Store_Item, Order, Order_Item, Shipping_Address, Customer

# Register your models here.
admin.site.register(Store_Item)
admin.site.register(Store_Image)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Order_Item)
admin.site.register(Shipping_Address)
