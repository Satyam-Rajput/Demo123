from django.db import models
from django.contrib.auth.models import User, UserManager


# Create your models here.
#Model for Book Table, will create a Table name books in the DB
class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50)

    def __str__(self):# to display the name of the book in the admin page
        return self.name

#Model for Order Table, will create a Table name Orders in the DB
class Order(models.Model):
    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
    )
    #creating a foreign key to reference the User who has placed the order
    custom_user = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,default=0
    )
    #limiting the choice of the user, creating a static dropdown to select
    type_choices=[('Rent','Rent'),('Purchase','Purchase')]
    status_choices = [
        ('Ready to checkout', 'Ready to checkout'),
        ('Payment Pending', 'Payment Pending'),
        ('Payment Completed', 'Payment Completed'),
        ('Order Placed', 'Order Placed'),
        ('Order Shipped', 'Order Shipped'),
        ('Delivered', 'Delivered'),


    ]
    type = models.CharField(max_length=50,choices=type_choices)
    status = models.CharField(max_length=50, choices=status_choices, default='Ready to checkout')

#Model for Transaction Table, will create a Table name Transactions in the DB

class Transaction(models.Model):
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,default=0
    )
    payment_choices=[
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('UPI', 'UPI'),
        ('E-Wallet', 'E-Wallet'),
        ('Net Banking', 'Net Banking'),
        ('Cash', 'Cash'),


    ]
    payment_method = models.CharField(max_length=50,choices=payment_choices,default='Credit Card')
    transaction_date = models.DateTimeField()
class CustomUser(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=0)
   
    
    phone_number=models.IntegerField()
    house_number=models.IntegerField()
    street_name=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField()
    # Use UserManager to get the create_user method, etc.

    

