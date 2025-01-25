from django.shortcuts import render, redirect, HttpResponseRedirect 
from django.contrib.auth.hashers import check_password  
from django.views import View 
from store.models import Order, Customer, Product

class Orders(View):
    
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')

        if cart:
            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)  # Fetch the Product object
                order = Order(
                    customer=Customer.objects.get(id=customer),
                    product=product,  # Link product to the order
                    address=address,
                    phone=phone,
                    quantity=quantity,
                )
                order.save()

        return redirect('orders')

    def get(self, request):
        
        customer_id = request.session.get('customer')
        
        if not customer_id:
            return redirect('login')            
        
        customer = Customer.objects.get(id=customer_id)
        orders = Order.objects.filter(customer=customer).order_by('-id')
        for order in orders:
            order.product_price = order.product.price
            order.total_price = order.product_price * order.quantity  # Calculate the total price

        return render(request, 'orders.html', {'orders': orders})

        
