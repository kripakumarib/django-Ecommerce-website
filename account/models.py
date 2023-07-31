from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

class CustUser(AbstractUser):
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="user_profile_pic",null=True)
    options=(
        ('Customer','Customer'),
        ('Store','Store')
    )
    user_type=models.CharField(max_length=10,choices=options,default='Customer')
class Company(models.Model):
    company_name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='com_logo_image')
class Product(models.Model):
    product_name=models.CharField(max_length=50,)
    product_image=models.ImageField(upload_to="product_images",verbose_name='product_image')
    productprice=models.IntegerField()
    productstock=models.IntegerField()
    pro_company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name="productcompany",null=True)


class Cart(models.Model):
    product_name=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_product')
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='cart_user')
    date=models.DateField(auto_now_add=True)

class Review(models.Model):
    review=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    rating=models.FloatField()
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='revie_user')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='revie_product')