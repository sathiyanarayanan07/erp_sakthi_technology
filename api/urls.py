

from django.urls import path
from . import views

urlpatterns = [
    path("single_login/",views.single_login,name="role1_login"),
    path("get_user_data/",views.get_user_data,name="get_user_data"),
    path("single_signup/",views.admin_single_signup,name="single_signup"),
    path("logout/",views.logout,name="logout")
   

  
]
