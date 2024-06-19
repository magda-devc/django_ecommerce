from django.urls import path
from . import views

app_name = 'plp_ecommerce'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('product_details/<int:pk>/', views.product_details, name= 'product_details'),
    path('product_list/', views.product_list,name = 'product_list' ),
    path('customer_details/<int:pk>/', views.customer_details, name='customer_details'),
    path('customer_list/', views.customer_list, name='customer_list'),

]