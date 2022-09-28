from django.db import models


class meetings(models.Model):
    admin_id=models.CharField(max_length=1000)  ##username of admin who created meeting
    title=models.CharField(max_length=1000,null=True)     ##
    description=models.CharField(max_length=1000,null=True)  ##
    ###participat details
    participant_name=models.CharField(max_length=1000,null=True)
    participant_email=models.CharField(max_length=1000,default="none")
    participant_notes=models.CharField(max_length=1000,null=True)

    time_slot=models.DateTimeField(null=False)      ##
    start_url=models.CharField(max_length=1000,null=True)     ###
    join_url=models.CharField(max_length=1000,null=True)      ###
    is_accepted=models.BooleanField(default=False)   



class participants(models.Model):
    join_url=models.CharField(max_length=1000,null=True) 
    name=models.CharField(max_length=100,null=True) 
    email=models.CharField(max_length=100,null=True)
    notes=models.CharField(max_length=1000,null=True) 