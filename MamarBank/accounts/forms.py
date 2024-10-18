from django.contrib.auth.forms import UserCreationForm
from .models import UserBankAccount,UserAddress
from django.contrib.auth.models import User
from django import forms
from .constants import Gender_type,Account_type

class UserRejistrationForm(UserCreationForm):
    # account_type=forms.CharField(max_length=20,choices=Account_type)
    # account_no=forms.IntegerField()
    account_type=forms.ChoiceField(choices=Account_type)
    birth_day=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    street_address=forms.CharField(max_length=100)
    gender=forms.ChoiceField(choices=Gender_type)
    city=forms.CharField(max_length=100)
    postal_code=forms.IntegerField()
    country=forms.CharField(max_length=100)

    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name','email',
                'gender','birth_day','postal_code','city','country','street_address','account_type']
        
        def save(self,commit=True):
            our_User=super().save(commit=False)
            if commit==True:
                our_User.save()
                Account_type=self.cleaned_data.get('account_type')
                account_no=self.cleaned_data.get('account_no')
                Gender_type=self.cleaned_data.get('Gender_type')
                postal_code=self.cleaned_data.get('postal_code')
                country=self.cleaded_data.get('country')
                birth_day=self.cleaned_data.get('birth_day')
                city=self.cleaned_data.get('city')
                street_address=self.cleaned_data.get('street_address')
                
                UserAddress.objects.create(
                    user=our_User,
                    postal_code=postal_code,
                    street_address=street_address,
                    city=city,
                    country=country
                )
                UserBankAccount.objects.create(
                    user=our_User,
                    Account_type=Account_type,
                    Gender_type=Gender_type,
                    birth_day=birth_day,
                    account_no=100000+our_User.id
                )
            return our_User
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                    'class':(
                        'appearance-none block w-full bg-gray-200 '
                        'text-gray-700 border border-gray-200 rounded '
                        'py-3 px-4 leading-tight focus:outline-none '
                        'focus:bg-white focus:border-gray-500 '
                    )
                })