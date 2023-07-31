from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from .models import *
from .forms import RegForm,LogForm
from django.contrib.auth import authenticate,login






# Create your views here.
class Mhome(TemplateView):
    template_name="mhome.html"


        #    kwargs['usertype'] = 'customer'
        #    return super().get_context_data(**kwargs)
        # def get_context_data(self, **kwargs):
        #  kwargs['usertype'] = 'store'
        #  return super().get_context_data(**kwargs)

# class LogView(TemplateView):
#         template_name="login.html"
#         form_class=LogForm 
#         def post(self,request,*args,**kwargs):
#             form_data=LogForm(data=request.POST)
#             if form_data.is_valid():
#                 uname=form_data.cleaned_data.get("username")
#                 pswd=form_data.cleaned_data.get("password")
#                 user=authenticate(request,username=uname,password=pswd)
#                 if user:
#                     login(request,user)
#                     messages.success(request,"login successful")
#                     return redirect("ch")
#                 else:
#                     messages.error(request,"login failed")
#                     return redirect('log')
#             else:
                
#                 return render(request,"login.html",{"form":form_data})

# class LogView(TemplateView):
#         template_name="login.html"
#         form_class=LogForm 
#         def post(self,request,*args,**kwargs):
#             form_data=LogForm(data=request.POST)
#             if form_data.is_valid():
#                 uname=form_data.cleaned_data.get("username")
#                 pswd=form_data.cleaned_data.get("password")
#                 user=authenticate(request,username=uname,password=pswd)
#                 if user:
#                       if user.usertype=="Store":
#                          login(request,user)
#                          messages.success(request,"login successful")
#                          return redirect("sh")  
#                       if user.usertype=="Customer":
#                          login(request,user)   
#                          return redirect("ch") 
#                 else:
#                      messages.error(request,"login failed")
#                      return redirect('log')
#             else: 
#                 return render(request,"login.html",{"form":form_data})
                
                   
  
                
        


class RegView(CreateView):
    template_name="registration.html"
    form_class=RegForm
    model=CustUser
    success_url=reverse_lazy("log")

class LogView(FormView):
    template_name="login.html"
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        data=LogForm(data=request.POST)
        print(data)
        if data.is_valid():
            uname=data.cleaned_data.get("username")
            pwd=data.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                if request.user.user_type=='Store':
                    return redirect("sh")
                else:
                    return redirect("ch")
            else:
                return redirect("login")      
        else:
            return redirect(request,"login.html",{"form":data})           
        
