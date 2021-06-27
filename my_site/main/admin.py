from django.contrib import admin
from .models import Item, Categories, Discount, Order, Comments

admin.site.register(Item)
admin.site.register(Categories)
admin.site.register(Discount)
admin.site.register(Order)
admin.site.register(Comments)
