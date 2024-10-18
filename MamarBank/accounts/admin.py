from django.contrib import admin
from accounts.models import UserBankAccount,UserAddress

# Register your models here.
admin.site.register(UserAddress)
admin.site.register(UserBankAccount)