from django.urls import path
from .views import *

urlpatterns=[
    path('reg/',RegView.as_view(),name="reg"),
    path('log/',LogView.as_view(),name="log")
    
]