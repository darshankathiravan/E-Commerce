from django.contrib import admin
from .models import Category, Customer, Product,Order

class OrdersAdmin(admin.ModelAdmin):
    readonly_fields = ('product_price',)  # Display product price in form (non-editable)
    list_display = ('product', 'product_price', 'customer', 'quantity', 'date', 'status')  # Show product price in the list
    
admin.site.register([Category, Customer, Product])
admin.site.register(Order, OrdersAdmin)  # Associate Orders with OrdersAdmin

