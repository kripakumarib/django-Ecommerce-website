from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View,TemplateView,CreateView,FormView,UpdateView,DeleteView
from account.models import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth.models import User
from .models import *




# # Create your views here.
# # class Uhome(TemplateView):
# #     template_name="userhome.html"
# # class Uhome(View):
# #     def get(self,request,args,*kwargs):
# #         return render('uh')

        
# class Logout(View):
#     def get(self,request):
#        logout(request)
#        return redirect('h')
    
# class Products(TemplateView):
#     template_name="products.html"



# class Addproductview(CreateView):
#     template_name='addproduct.html'
#     form_class=ProductForm
#     model=Addproducts
#     success_url=reverse_lazy("vpro")
#     def post(self,request,*args,**kwargs): 
#         form_data=self.form_class(request.POST) 
#         if form_data.is_valid():
#             messages.success(request,"product added!!!") 
#             return  redirect('vprod') 
#         else:
#             messages.error(request,"Failed")
#             return render(request,'AddProducts.html',{'form':'form_data'})
            


# # class EditProfileView(View):
# #    def get(self,request,args,*kwargs):
# #       pid=kwargs.get("pid")
# #       p=UserProfile.objects.get(id=pid)
# #       f=ProfileForm(instance=p)
# #       return render(request,"editprofile.html",{"form":f})
# #    def post(self,request,args,*kwargs):
# #       pid=kwargs.get("pid")
# #       p=UserProfile.objects.get(id=pid)
# #       form_data=ProfileForm(data=request.POST,files=request.FILES,instance=p)
# #       if form_data.is_valid():
# #          form_data.save()
# #          messages.success(request,"profile updated")
# #          return redirect("pro")
# #       else:
# #          return render(request,"edit.html",{"form":form_data})
      



# class Shome(CreateView):
#     form_class=ProductForm
#     template_name="storehome.html"
#     model=Products
#     success_url=reverse_lazy("sh")
#     def form_valid(self,form):
#         form.instance.user=self.request.user
#         self.object=form.save()
#         messages.success(self.request,"product Posted!")
#         return super().form_valid(form)
#     # def get_context_data(self,**kwargs):
#     #     context=super().get_context_data(**kwargs)
#     #     # context["data"]=Products.objects.all().order_by("-name")
#     #     context["cform"]=ProductForm()
#     #     context["review"]=Products.objects.all()
#     #     return context

   




# class Viewproducts(TemplateView):
#     template_name="viewproduct.html"

# class Viewreview(TemplateView):
#     template_name="viewreview.html"
#     def get_context_data(self,**kwargs):
#         context=super().get_context_data(**kwargs)
#         context["data"]=Products.objects.filter(user=self.request.user)
#         return context
# class Totalproduct(CreateView):
#     def get(self,request):
#         data=Addproducts.objects.all()
#         return render(request,"viewproducts.html",{"data":data})

# class Editproduct(View):
#     def get(self,request,*args,**kwargs):
#         di_d=kwargs.get('did')
#         item=Addproducts.objects.get(id=di_d)
#         form=ProductForm(isinstance=item)
#         return render(request,"edit.html",{'form:form'})
#     def post(self,request,*args,**kwargs):
#         di_d=kwargs.get('did')
#         item=Addproducts.objects.get(id=di_d)
#         form_data=ProductForm
#         if form_data.is_valid():
#             form_data.save()
#             return redirect('vpro')
#         else:
#             return redirect('addpro')
# class DeleteProduct(View):
#     def get(self,request,*args,**kwargs):
#         did=kwargs.get('did')
#         item=Addproducts.objects.get(id=did)
#         item.delete()
#         return redirect('vpro')
   

# Create your views here.
class Staff_home(TemplateView):
    template_name="storehome.html"
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["data"] =Company.objects.all()
       return context
   
class Add_brand(CreateView):
    template_name="addbrand.html"
    form_class=Brand_form
    model=Company
    success_url=reverse_lazy("sh") 
    def post(self, request,args,*kwargs):
        form_data=self.form_class(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.instance.user=self.request.user
            form_data.save()
            messages.success(self.request,"brand added successfully")
            return redirect('add_brand')
        else:
            return render(request,"add_brand.html",{"form":form_data})
  
  
class Product_view(TemplateView):
    template_name="viewproduct.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] =Product.objects.filter(pro_company_id=self.kwargs.get('id')) 
        return context
    
class Add_product(CreateView):
    template_name="addproduct.html"
    form_class=Product_form
    model=Product
    success_url=reverse_lazy("sh")
    def form_valid(self, form):
        form.instance.pro_company=Company.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)
  
class Edit_product(UpdateView):
    form_class=Product_form
    template_name="edit.html"
    model=Product
    pk_url_kwarg="pk"
    success_url=reverse_lazy("sh")
    def form_valid(self, form):
        self.object=form.save()
        return super().form_valid(form)

