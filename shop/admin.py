from msilib.schema import Class
from django.contrib import admin
from .models import *
# Register your models here.


class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description')


class productAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'image', 'name', 'description', 'rating', 'rating_count',
                    'offerPrice', 'originalPrice', 'priceDifference')


admin.site.register(catagory, categoryAdmin)
admin.site.register(products, productAdmin)
