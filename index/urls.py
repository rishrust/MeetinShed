from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('register/otp_verify',views.otp_ver,name='otp_verification'),
    
    path('logged_in/',include("LOGIN.urls"),name="logged_in"),
    path('joinmeeting',views.joinmeeting,name='joinmeeting'),
    path('create_meeting',views.create_meeting,name="create_meeting"),
    
    #path('testing',views.testing,name='testing'),
]