from django.shortcuts import render,redirect,HttpResponse
# import google_calender

# Create your views here.
def create_event_admin(request,meet_id):
    google_calender.calender_setup.get_calendar_service()
    return HttpResponse("hello")
