from django.contrib import admin

from shop.models import Category, Product
from django import HttpResponse
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)