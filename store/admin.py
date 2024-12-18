from django.contrib import admin
from .models import Category, Customer, Products,Orders

class OrdersAdmin(admin.ModelAdmin):
    readonly_fields = ('product_price',)  # Display product price in form (non-editable)
    list_display = ('product', 'product_price', 'customer', 'quantity', 'date', 'status')  # Show product price in the list
    
admin.site.register([Category, Customer, Products])
admin.site.register(Orders, OrdersAdmin)  # Associate Orders with OrdersAdmin

