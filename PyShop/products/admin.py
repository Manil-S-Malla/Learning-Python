from django.contrib import admin
from . models import Product, Offer

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')



admin.site.register(Product, ProductAdmin)            #   Registers the 'ProductAdmin' class of 'Product' module to the 'site' class of the 'admin' app.   
admin.site.register(Offer, OfferAdmin)            #   Registers the 'OfferAdmin' class of 'Offer' module to the 'site' class of the 'admin' app.   
