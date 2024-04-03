import jwt
import requests
import json
from time import time

zoom_credential={"starturl":"","joinurl":"",}
def create_schedule(title,starttime):
    API_KEY = ''
    API_SEC = ''

    meetingId = 11


    def generateToken():
        token = jwt.encode(
            {'iss': API_KEY, 'exp': time() + 5000},
            API_SEC,
            algorithm='HS256'
        )
        return token

    meetingdetails = {"topic": title,
                    "type": 2,
                    "start_time": starttime,
                    "duration": "30",
                    "timezone": "Asia/Calcutta",
                    "agenda": "test",
                    "password":"1234",

                    "recurrence": {"type": 1,
                                    "repeat_interval": 1
                                    },
                    "settings": {"host_video": "true",
                                "participant_video": "true",
                                "join_before_host": "False",
                                "mute_upon_entry": "False",
                                "watermark": "true",
                                "audio": "voip",
                                "auto_recording": "cloud"
                                }
                    }
    def createMeeting():
        headers = {'authorization': 'Bearer %s' % generateToken(),
                'content-type': 'application/json'}
        r = requests.post(
            f'https://api.zoom.us/v2/users/me/meetings', headers=headers, data=json.dumps(meetingdetails))

        print("\n creating zoom meeting ... \n")
        #print(r.text)
        y=json.loads(r.text)
        start_url=y["start_url"]
        join_url= y["join_url"]
        # meet_password=y["password"]
        zoom_credential["joinurl"]=join_url
        zoom_credential["starturl"]=start_url
        # print(start_url)
        # print(join_Url)
        # print(meet_password)

    createMeeting()
    return zoom_credential
