from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='logged_in'),
    path('logout',views.logout,name='logout'),
    #path('create_meetings/<str:>',views)
    path('create_meeting',views.create_meeting,name="create_meeting"),
    path('joinmeeting',views.joinmeeting,name='joinmeeting'),
    path('mymeetings',views.mymeetings,name='mymeetings'),
    #path('/testing/',views.testing,name='testing'),

]
