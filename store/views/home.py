from django.shortcuts import render, redirect, HttpResponseRedirect 
from store.models import Product 
from store.models import Category 
from django.views import View 


# Create your views here. 
class Index(View): 

	def post(self, request): 
		product = request.POST.get('product') 
		remove = request.POST.get('remove') 
		cart = request.session.get('cart') 
		if cart: 
			quantity = cart.get(product) 
			if quantity: 
				if remove: 
					if quantity <= 1: 
						cart.pop(product) 
					else: 
						cart[product] = quantity-1
				else: 
					cart[product] = quantity+1

			else: 
				cart[product] = 1
		else: 
			cart = {} 
			cart[product] = 1
		
		request.session['cart'] = cart 
		print('cart', request.session['cart']) 
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

	def get(self, request): 
		# print() 
		return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}') 


def store(request): 	
	cart = request.session.get('cart') 
	if not cart: 
		request.session['cart'] = {} 
	products = None
	categories = Category.get_all_categories() 
	categoryID = request.GET.get('category') 
	if categoryID: 
		products = Product.get_all_products_by_categoryid(categoryID) 
	else: 
		products = Product.get_all_products() 
	data = {
        'products': products,
        'categories': categories,
        'cart' : cart,
    }
	
	print('you are : ', request.session.get('name')) 
	return render(request, 'index.html', data) 
