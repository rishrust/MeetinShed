from datetime import datetime
import random
import smtplib ## to create server and login it in
##installed validate-email-address   pip
##installed py3dns                    pip

from validate_email_address import validate_email



def is_email_exists(email):
    isExists = validate_email(email, verify=True)
    status=str(isExists)
    return status





def create_otp(user):
    email='rishabhsinghastic@gmail.com'
    server=smtplib.SMTP('smtp.gmail.com',587)
    #adding TLS security 
    server.starttls()
    #get your app password of gmail ----as directed in the video
    password='sykfjaeepbafawdv'
    server.login(email,password)
    #generate OTP using random.randint() function
    otp=''.join([str(random.randint(0,9)) for i in range(4)])
    msg='Your OTP to Register to MeetinShed is'+str(otp)
    sender='rishabhsinghastic@gmail.com'  #write email id of sender
    receiver=user #write email of receiver
    #sendi
    server.sendmail(sender,receiver,msg)
    server.quit()
    return otp


#create_otp()



# def meeting_generated(user_email,title,date,share_link):
#     email='meetinshed@gmail.com'
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     #adding TLS security 
#     server.starttls()
#     #get your app password of gmail ----as directed in the video
#     password='sykfjaeepbafawdv'
#     server.login(email,password)
#     #generate OTP using random.randint() function
#     msg='Your Meeting '+str(title)+' on '+str(date)+'\n is scheduled, now awaiting for recievers conformation\n Share this link with other person to invite them on meeting '+str(share_link)+'\n\n Meeting genrated on '+str(datetime.now)
#     sender='meetinshed@gmail.com'  #write email id of sender
#     receiver=user_email #write email of receiver
#     #sendi
#     server.sendmail(sender,receiver,msg)
#     server.quit()



# def meetingconformed(user_email,meeting_details):
#     email='meetinshed@gmail.com'
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     #adding TLS security 
#     server.starttls()
#     #get your app password of gmail ----as directed in the video
#     password='sykfjaeepbafawdv'
#     server.login(email,password)
#     #generate OTP using random.randint() function
#     msg="Your Meeting "+str(meeting_details["title"])+' on '+meeting_details["date"]+"is accepted by "+meeting_details["participant_name"]+"\n\n"+"\n\n This meeting was conformed by "+meeting_details["participant_mail"]+" on "+str(datetime.now)+"\n\nParticipant Notes"+meeting_details["participant_notes"]+"\n\nThank You For Using MeetinShed"
#     sender='meetinshed@gmail.com'  #write email id of sender
#     receiver=user_email #write email of receiver
#     #sendi
#     server.sendmail(sender,receiver,msg)
#     server.quit()