from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginpage,name="loginpage"),
    #customer1 url
    path('customer1',views.customer1,name="customer1"),
    #customer2 url
    path('customer2',views.customer2,name="customer2"),
    #cadmin url
    path('adminpage',views.adminpage,name="adminpage"),
]