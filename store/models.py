from django.db import models
from django.conf import settings
import datetime
# Create your models here.

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title= models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL,null=True,related_name='+')


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug =  models.SlugField()
    # 9999999.99
    unit_price =  models.DecimalField(decimal_places=2, max_digits=9)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S" 
    MEMBERSHIP_GOLD = "G"
    MEMBERSHIP_CHOICES = {
        MEMBERSHIP_GOLD: 'Gold',
        MEMBERSHIP_BRONZE: 'Bronze',
        MEMBERSHIP_SILVER: 'Silver',
    }
    
    # Link to Django's User model (or custom User if you have one)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Customer-specific fields only
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    @property
    def first_name(self):
        return self.user.first_name
    
    @property
    def last_name(self):
        return self.user.last_name
    
    @property
    def email(self):
        return self.user.email


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = {
        PAYMENT_STATUS_PENDING:'Pending',
        PAYMENT_STATUS_COMPLETE:'Complete',
        PAYMENT_STATUS_FAILED:'Failed',
    }
    placed_at =models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=2, choices = PAYMENT_STATUS_CHOICES, default= PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=9)
    # Relationships 
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


class CartItem(models.Model):
    quantity = models.PositiveSmallIntegerField()
    # Relationships 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

# One to one relationship
# class Address(models.Model):
#     street = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

# One to many relationship
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zip_code = models.PositiveBigIntegerField(default=00000)


