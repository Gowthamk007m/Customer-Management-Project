from django.forms import ModelForm
from  .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django.contrib.auth.models import User


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields='__all__'
        exclude=['user']

        

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields=['status']

class User_update(ModelForm):
    class Meta:
        model = Order
        fields=['product','status']
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']