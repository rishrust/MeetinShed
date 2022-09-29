from contextlib import redirect_stderr
from http.client import HTTPResponse
from pickletools import read_uint1
from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpRequest ## for creating http request
from django.contrib import messages
from django.contrib.auth.models import User, auth
from LOGIN.models import meetings
from LOGIN.models import participants
from . import email_server
# Create your views here.



##we will redirect if user tries to request homepage to his logged in page
def home(request):
    if request.user.is_authenticated:
        return redirect("logged_in")
    else:
        return render(request,'index.html')



#####################FOR LOGIN REGISTER LOGOUT#########################
#STUPID OTP METHOD
# username=""
# firstname=""
# lastname=""
# otp=""
# email=""
# password=""

def register(request):
    #STUPID OTP METHOD
    # global username
    # global firstname
    # global lastname
    # global otp
    # global email
    # global password
    if request.method=='POST':
        if request.POST['password']==request.POST['passwordr']:
            
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")#message automatically 
                return redirect('register')                      #passed in redirect 
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('register')## THIS REDIRECT IS NAME OF THE URL PATCHER

            else: #### we will check if email exists or not
                email_status=email_server.is_email_exists(email)
                if email_status=="True":
                    otp=email_server.create_otp(email)

                    otpfile=open("otp.txt","w+")
                    otpfile.write(otp+"\n")
                    otpfile.write(username+"\n")
                    otpfile.write(firstname+"\n")
                    otpfile.write(lastname+"\n")
                    otpfile.write(password+"\n")
                    otpfile.write(email+"\n")
                    otpfile.close()
                    return redirect('otp_verification')
                    
                else:
                    messages.info(request,"Enter a Valid Email Address")
                    return redirect('register')
        else:
            messages.info(request,"Password Dosent Match")
            return redirect('register')
    return render(request,"register.html")


def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method=="POST":
            email=request.POST['email']
            password=request.POST['password']
            if(User.objects.filter(email=email).exists()):
                username=User.objects.get(email=email).username
                userauth = auth.authenticate(username=username,password=password) ##for verification
                if userauth is not None:
                    auth.login(request,userauth) ##passing login info
                    userid=str(User.objects.get(email=email).id)
                    return redirect('logged_in')
                else:
                    messages.info(request,"Invalid Credentials")
                    return redirect('login')
            else:
                messages.info(request,"User Not Registered")
                return redirect('logged_in')
        return render(request,'login.html')





def otp_ver(request):
    #STUPID OTP METHOD
    # global username
    # global firstname
    # global lastname
    # global otp
    # global email
    # global password
    otpfile=open("otp.txt","r") 
    otp=(otpfile.readline()).rstrip("\n")
    
    if otp!="":
        username=(otpfile.readline()).rstrip("\n")
        firstname=(otpfile.readline()).rstrip("\n")
        lastname=(otpfile.readline()).rstrip("\n")
        password=(otpfile.readline()).rstrip("\n")
        email=(otpfile.readline()).rstrip("\n")
        otpfile.close()
        print(otp)
        if request.method=="POST":
            userotp=request.POST["userotp"]
            
            if otp == userotp:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save()##creating sving objects
                # username=""
                # firstname=""
                # lastname=""
                # otp=""
                # email=""
                # password=""
                otpfile=open("otp.txt","w+")
                otpfile.close() ##cleanign otpfile
                 
                messages.info(request,"Login To Continue")
                return redirect("login")
            else:
                messages.info(request,"Wrong OTP")
                render(request,'otp.html')

        return render(request,'otp.html')
    else:
        return redirect("home")



def joinmeeting(request):
    participant=request.POST['participant']
    email=request.POST["email"]
    des=request.POST["notes"]
    joinurl=request.POST["joinurl"]
    if(meetings.objects.filter(join_url=joinurl).exists()):
        meeting=meetings.objects.get(join_url=joinurl)
        email_exist=meeting.participant_email
        if email_exist=="none":
            obj=participants.objects.create(join_url=joinurl,notes=des,email=email,name=participant)
            meet=meetings.objects.get(join_url=joinurl)
            meet.participant_names=participant
            meet.participant_email=email
            meet.participant_notes=des
            meet.is_accepted=True
            meet.save()
            obj.save()
            return redirect(joinurl)
        elif email_exist==email:
            return redirect(joinurl)
        else:
            messages.info(request,"Meeting Already Booked")
            return render(request,"error.html")

    else:
        messages.info(request,"404 LINK INVALID")
        return render(request,"error.html")
    




##for failsafe if user clicks on schedule meeting and sends reqeust from homepage then redirect him to 
## logged in page
def create_meeting(request):
    if request.user.is_authenticated:
        redirect("logged_in")
    else:
        messages.info(request,"Login To Shedule Meetings")
        return redirect('login')
##########################################end regiteration####################################

# def testing(request):
#     if request.method=='POST':
#         dt=request.POST['dt']
#         dtstr=str(dt).rstrip("+00:00")
#         obj=meetings.objects.create(time_slot=)
#         finstr=datetime.strptime(dtstr, format)
#         #k=meetings.objects.get(id=1).time_slot
#         #date=datetime.datetime(b[int(0:2),int]).strftime("%Y-%m-%dT%H:M:%Sz")
#         print(finstr)
#         #print(str(k).rstrip("+00:00"))

      
#         #print(dt)
#         return redirect('testing')   
    #return render(request,'demoslots.html')
