from django import forms
from account.models import *



# class ProductForm(forms.ModelForm):
#     class Meta:
#         model=Product
#         fields=("name","price","description","image","productcompany","image")


        
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=('review',)
        widgets={
            'review':forms.Textarea(attrs={"class":"form-control"})
           
        }
        
       
