from django import forms
from .models import CustUser
from django.contrib.auth.forms import UserCreationForm




class RegForm(UserCreationForm):
    class Meta:
        model=CustUser
        fields=['first_name','last_name','email','username','phone','address','profile_pic','user_type','password1','password2']
        widgets={
            'phone':forms.NumberInput(),
            'address':forms.Textarea(),
        }
class LogForm(forms.Form):
    username=forms.CharField(max_length=100,label="USERNAME",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter your username"}))
    password=forms.CharField(max_length=100,label="PASSWORD",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter your password"}))     