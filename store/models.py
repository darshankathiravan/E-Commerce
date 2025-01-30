from django.db import models
import datetime
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    @staticmethod
    def get_all_categories():
       return Category.objects.all()
        
    def __str__(self):
        return self.name

class Customer(models.Model): 
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50) 
    phone = models.CharField(max_length=20) 
    email = models.EmailField(max_length=50) 
    password = models.CharField(max_length=100) 

    # to save the data 
    def register(self):
        self.save() 
    
    @staticmethod
    def get_customer_by_email(email): 
        try: 
            return Customer.objects.get(email=email) 
        except: 
            return False 

    def isExists(self): 
        if Customer.objects.filter(email=self.email): 
            return True
        return False
    
    def __str__(self):
        return self.first_name
    

class Product(models.Model): 
    name = models.CharField(max_length=60) 
    price = models.IntegerField(default=0) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
    description = models.CharField(max_length=250, default='', blank=True, null=True) 
    image = models.ImageField(upload_to='uploads/products/') 

    @staticmethod
    def get_products_by_id(ids): 
        return Product.objects.filter(id__in=ids) 

    @staticmethod
    def get_all_products(): 
        return Product.objects.all() 

    @staticmethod
    def get_all_products_by_categoryid(category_id): 
        if category_id: 
            return Product.objects.filter(category=category_id) 
        else: 
            return Product.get_all_products() 
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    address = models.CharField(max_length=255, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)

    def product_price(self):
        return self.product.price

    def __str__(self):
        return f"Order: {self.product.name} by {self.customer.first_name} ({self.date})"

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    def product_price(self):
        return self.product.price
        
    def __str__(self):
        return self.product.name + "order"
    
    def save(self, *args, **kwargs):
        """ 
        Set the order price only when the order is created 
        """
        if not self.pk:  # If the order is being created, set the product's price
            self.price = self.product.price  # Copy the product price only on creation
        super().save(*args, **kwargs)  # Call parent save method
        
    @staticmethod    
    def get_order_id(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')