from django.urls import path
from .views import *

urlpatterns = [
    # path('customer/',Chome.as_view(),name="ch"),
    # path('addcart/',Addcart.as_view(),name="addcart"),
    # path('addreview/',Addreview.as_view(),name="addreview"),
    # path('viewproduct/',Viewproducts.as_view(),name="viewpro"),
    path('buyproduct/',Buyproducts.as_view(),name="buypro"),
    path('logout/',Logout.as_view(),name="logout"),
    path('customer_home/',Cust_home.as_view(),name="ch"),
    path('view_product/<int:id>',Product_view.as_view(),name="cview_product"),
    path('add_review/',add_review.as_view(),name="cadd_review"),
    path('product_details/<int:id>',Product_details.as_view(),name="product_details"),
 
]
