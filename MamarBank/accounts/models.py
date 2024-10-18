from django.db import models
from django.contrib.auth.models import User
from accounts.constants import Account_type,Gender_type

# Create your models here.
class UserBankAccount(models.Model):
    user=models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    account_type=models.CharField(max_length=20,choices=Account_type)
    account_no=models.IntegerField(unique=True)
    birth_day=models.DateField(blank=True,null=True)
    Gender=models.CharField(max_length=20,choices=Gender_type)
    email=models.EmailField(unique=True,blank=True,null=True)
    initial_deposite_data=models.DateField(auto_now_add=True)
    Balance=models.DecimalField(default=0,max_digits=12,decimal_places=2)
    def __str__(self) -> str:
        return str( self.account_no)

class UserAddress(models.Model):
    user=models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    country=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.user.email
