from django.urls import path
from .views import *

# urlpatterns = [
# #     path('store/',Shome.as_view(),name="sh"),
# #     path('product/',Products.as_view(),name="pro"),
# #     path('viewproducts/',Viewproducts.as_view(),name="vpro"),
# #     path('viewreview/',Products.as_view(),name="viewreview"),
# #     path('addproduct/',Addproductview.as_view(),name="addpro"),
# #     path('logout/',Logout.as_view(),name="logout"),
# #     path('editproduct/<int:pk>',Editproduct.as_view(),name="eproduct"),
# #     path('deleteproduct/<int:pk>',DeleteProduct.as_view(),name="dproduct"),
# # ]
urlpatterns = [
    path('staff_home/',Staff_home.as_view(),name="shome"),
    path('add_brand_staff/',Add_brand.as_view(),name="add_brand"),
    path('view_product/<int:id>',Product_view.as_view(),name="view_product"),
    path('add_product/<int:pk>',Add_product.as_view(),name="add_product"),
    path('edit_product/<int:pk>',Edit_product.as_view(),name="edit_product"),
   
]