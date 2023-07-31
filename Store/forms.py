from django import forms
from account.models import *



# class ProductForm(forms.ModelForm):
#     class Meta:
#         model=Product
#         fields=("product_name","price","description","productimage","company")


        
# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model=Review
#         fields=('review',)
#         widgets={
#             'review':forms.Textarea(attrs={"class":"form-control"})
#         }
class Brand_form(forms.ModelForm):
    class Meta:
        model=Company
        fields='__all__'

class Product_form(forms.ModelForm):
    class Meta:
        model=Product
        exclude=['pro_company']
        
        

