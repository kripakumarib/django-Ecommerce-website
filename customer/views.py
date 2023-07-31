from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View,TemplateView,CreateView,FormView,UpdateView,DeleteView
from account.models import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth.models import User
   



# class Chome(CreateView):
#     template_name="customerhome.html"
#     form_class=ProductForm
#     model=Products
#     success_url=reverse_lazy("ch")
#     def form_valid(self,form):
#         form.instance.user=self.request.user
#         self.object=form.save()
#         messages.success(self.request,"product Posted!")
#         return super().form_valid(form)




# # Create your views here.
# # class Uhome(TemplateView):
# #     template_name="userhome.html"
# # class Uhome(View):
# #     def get(self,request,args,*kwargs):
# #         return render('uh')

        
class Logout(View):
    def get(self,request):
       logout(request)
       return redirect('h')
    
# # class Products(TemplateView):
# #     template_name="products.html"



# class Addcart(CreateView):
#     template_name='addcart.html'
#     form_class=ProductForm
#     model=Products
#     success_url=reverse_lazy("addpro")
#     def post(self, request,args,*kwargs):
#         form_data=self.form_class(data=request.POST,files=request.FILES)
#         if form_data.is_valid():
#             form_data.instance.user=self.request.user
#             form_data.save()
#             messages.success(self.request,"product added successfully")
#             return redirect('pro')
#         else:
#             return render(request,"addproduct.html",{"form":form_data})


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
      



#     # def get_context_data(self,**kwargs):
#     #     context=super().get_context_data(**kwargs)
#     #     context["data"]=Products.objects.all().order_by("-date")
#     #     context["rform"]=ReviewForm()
#     #     context["review"]=Review.objects.all()
#     #     return context

   




# class Viewproducts(TemplateView):
#     template_name="viewproducts.html"

class Buyproducts(TemplateView):
    template_name="buyproducts.html"
    

# class Addreview(TemplateView):
#     template_name="addreview.html"
#     form_class=ReviewForm
#     model=Review
#     success_url=reverse_lazy("ch")
# def addcomment(request,*args,**kwargs):
#     if request.method=="post":
#         bid=kwargs.get("bid")
#         product=Products.objects.get(id=bid)
#         user=request.user
#         review=request.POST.get("review")
#         Review.objects.create(review=review,user=user,product=product)
#         messages.success(request,"review submitted!")
#         return redirect("ch") 
#     messages.success(request,"review submitted failed!")
#     return redirect("uh")
    







# Create your views here.
class Cust_home(TemplateView):
    template_name="customerhome.html"
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["data"] =Company.objects.all()
       return context
   
class Product_view(TemplateView):
    template_name="cviewproduct.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] =Product.objects.filter(pro_company_id=self.kwargs.get('id')) 
        return context
    
class add_review(FormView):
    template_name="viewreview.html"
    form_class=ReviewForm
    
class Product_details(TemplateView):
    template_name="productdetail.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] =Product.objects.get(id=self.kwargs.get('id'))
        return context
    