from django.contrib import admin

from shop.models import CustomUser, Product, Order

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Order)
