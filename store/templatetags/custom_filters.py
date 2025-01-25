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
def get_item_quantity(cart, product_id):
    return cart.get(str(product_id), 0)