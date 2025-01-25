from django.contrib import admin 
from django.urls import path
from .views.login import Login, logout
from .views.signup import Signup
from .views.home import Index,store
from .views.orders import Orders

urlpatterns = [ 
    path('login/', Login.as_view(), name='login'), 
    path('logout/', logout, name='logout'), 
    path('store', store, name='store'), 
    path('signup/', Signup.as_view(), name='signup'), 
    path('', Index.as_view(), name='homepage'), 
    path('orders/', Orders.as_view(), name='orders'), 
] 