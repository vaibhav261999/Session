from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name='home'),
    path("Signup/",Signup,name='Signup'),
    path("Login/",Login,name='Login'),
    path("about/",about,name='about'),
    path("Contact/",Contact,name='Contact'),
    path("Services/",Services,name='Services'),
    
    path("savedata/",savedata,name='savedata'),
    path("Login_data/",Login_data,name='Login_data'),
    path("delete/",delete,name='delete'),

]

