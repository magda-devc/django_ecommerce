from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=20, blank=False, null=False)
    price = models.CharField(max_length=10, blank=False, null=False)
    image = models.ImageField(upload_to='product_details/')
    availability = models.BooleanField(default=True)
    #DecimalField(max_decimal)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return print(f"Hello {self.firstName} {self.lastName} {self.email}")