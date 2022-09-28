
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from .email_server import meeting_generated,meetingconformed
from .models import meetings,participants
from . import python_zoom_api   #### this is script for creating zoom links
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        username=request.user.username
        user=User.objects.get(username=username)
        user_meetings=meetings.objects.filter(admin_id=username)
        user_info={"username":user.username,"email":user.email,"firstname":user.first_name,"lastname":user.last_name}
        return render(request,'index.html',user_info)
    else:
        return redirect("login")



def mymeetings(request):
    if request.user.is_authenticated:

        username=request.user.username
        user_meetings=meetings.objects.filter(admin_id=username)
        return render(request,"mymeetings.html",{"mymeetings":user_meetings})
    else:
        return redirect("login")


def create_meeting(request):
    username=request.user.username
    user_email=User.objects.get(username=username).email
    ##defingig meeting attibutes
    meeting_title=request.POST['meet_title']
    des=request.POST['description']
    time_slot=request.POST['time_slot']

    ##creating object
    meet=meetings.objects.create(description=des,time_slot=time_slot,title=meeting_title,admin_id=username)
            
    ##creating zoom objects
    zoomdt=time_slot[0:14]+' '+time_slot[14:16]+': 00'
    zoomtitle=str(meeting_title)
    zoomurls=python_zoom_api.create_schedule(zoomtitle,zoomdt)

    ##saving urls in database
    meet.start_url=zoomurls["starturl"]
    meet.join_url=zoomurls["joinurl"]
    meet.save()
    # meeting_generated(user_email,str(meeting_title),str(time_slot),str(zoomurls["joinurl"]))
    messages.info(request,"Go in MyMeetings to check url")
    return redirect("mymeetings")
    
def joinmeeting(request):
    participant=request.POST['participant']
    email=request.POST["email"]
    des=request.POST["notes"]
    joinurl=request.POST["joinurl"]
    if(meetings.objects.filter(join_url=joinurl).exists()):
        meeting=meetings.objects.get(join_url=joinurl)
        if meeting.is_accepted==False:
            obj=participants.objects.create(join_url=joinurl,notes=des,email=email,name=participant)
            meet=meetings.objects.get(join_url=joinurl)
            meet.participant_name=participant
            meet.participant_email=email
            meet.participant_notes=des
            meet.is_accepted=True
            meet.save()
            obj.save()
            #####sending mail to admin about meeting####
            # meeting=meetings.objects.get(join_url=joinurl)
            # admin_email=User.objects.get(username=meeting.admin_id)
            # admin_email=admin_email.email
            # meeting_details={
            #     "title":meeting.title,
            #     "date":meeting.time_slot,
            #     "participant_name":meeting.participant_name,
            #     "participant_email":meeting.participant_name,
            #     "participant_notes":meeting.participant_notes,
            # }
            # meetingconformed(admin_email,meeting_details)
            ###################################
            return redirect(joinurl)
        else:
            messages.info(request,"This Meeting is already Booked")
            return render(request,"error.html")

    else:
        messages.info(request,"404 LINK INVALID")
        return render(request,"error.html")



def testing(request,userid):
    obj=meetings.objects.get(id=1)
    datetime=str(obj.time_slot)
    zoomdt=datetime[0:14]+' '+datetime[13:16]+': 00'
    print(zoomdt)
    print(datetime)
    return HttpResponse("de")




def logout(request):
    auth.logout(request)
    return redirect('home')


# 0123456789 
# 2022-09-13 18:59    database format
## "2022-09-25T12: 15: 00" zoomformat
##  2022-09-08T02:34  postformat
##  2022-09-13T18: 59: 00