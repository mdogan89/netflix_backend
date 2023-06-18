from django.urls import path
from .views import *

urlpatterns = [
    path("",register,name="register"),
    path("login",userLogin,name="login"),
    path("browse",profiles,name="profiles"),
    path("create-profile",createProfile,name="create-profile"),
    path("logout",logoff,name="logout"),
    path("profile",profile,name="profile"),
    path("delete",deleteUser,name="delete"),
]