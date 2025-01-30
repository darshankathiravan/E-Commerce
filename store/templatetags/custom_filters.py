from django import template
from store.models import Product

register = template.Library()

@register.filter
def product_name_by_id(product_id):
    try:
        product = Product.objects.get(id=product_id)
        return product.name
    except Product.DoesNotExist:
        return "Product not found"
    
@register.filter
def get_item_quantity(cart, item_id):
    if cart is None:
        return 0
    item_id_str = str(item_id)  # Convert to string
    item_id_int = int(item_id)  # Convert to int (in case cart uses integers)
    return cart.get(item_id_str, cart.get(item_id_int, 0))  # Check both types
