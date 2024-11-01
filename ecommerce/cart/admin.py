from django.contrib import admin
from cart.models import Cart,Payment
from cart.models import Order_details

# Register your models here.
admin.site.register(Cart)
admin.site.register(Order_details)
admin.site.register(Payment)