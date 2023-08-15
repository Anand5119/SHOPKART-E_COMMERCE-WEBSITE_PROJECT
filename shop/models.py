from django.db import models
import datetime
import os
from django.contrib.auth.models import User

# Create your models here.


def getFilename(request, filename):
    now_time = datetime.datetime.now().strftime("(%d-%m-%Y_%I.%M_%p_)")
    new_filename = '%s%s' % (now_time, filename)
    return os.path.join('upload/', new_filename)


class catagory(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFilename, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class products(models.Model):
    category = models.ForeignKey(catagory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFilename, null=True, blank=True)
    description = models.CharField(max_length=500, null=False, blank=False)
    rating = models.FloatField(default=0, null=False, blank=False)
    rating_count = models.IntegerField(default=0, null=False, blank=False)
    quantity = models.IntegerField(null=True, blank=False)
    offerPrice = models.IntegerField(null=False, blank=False)
    originalPrice = models.IntegerField(null=False, blank=False)
    priceDifference = models.IntegerField(null=False, blank=False)
    status = models.BooleanField(default=False, null=False)
    hotProducts = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    product_qty = models.IntegerField(
        null=False, blank=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
