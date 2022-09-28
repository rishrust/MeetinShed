from django.urls import path,include
from . import views
urlpatterns = [
    path('<str:meet_id>/logcal',views.create_event_admin,name='logcal'),
]