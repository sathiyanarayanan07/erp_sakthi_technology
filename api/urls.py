

from django.urls import path
from . import views

urlpatterns = [
    path("single_login/",views.single_login,name="role1_login"),
    path("get_user_data/",views.get_user_data,name="get_user_data"),
    path("single_signup/",views.single_signup,name="single_signup"),
    path("add_product_details/",views.add_product_details,name="add_product_details"),
    path("get_product_details/",views.get_product_details,name="get_product_details"),
    path("update_product_status/<int:id>/",views.update_product_status,name="update_product_status"),
    path("delete_product/<int:id>/",views.delete_product,name="delete_product"),
   

  
]
