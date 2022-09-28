import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

## creating credential file
creds={"installed":{"client_id":"124372208418-4eubm8cq7q2slfkv9osvjt68940qk9ur.apps.googleusercontent.com","project_id":"meetinshed","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"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","redirect_uris":["http://localhost"]}}
json_object = json.dumps(creds)

#os.remove('token.pickle')
with open("creds.json", "w") as outfile:
    outfile.write(json_object)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = "creds.json"

def get_calendar_service():
   creds = None
   # The file token.pickle stores the user's access and refresh tokens, and is
   # created automatically when the authorization flow completes for the first
   # time.
   if os.path.exists('token.pickle'):
       with open('token.pickle', 'rb') as token:
           creds = pickle.load(token)
   # If there are no (valid) credentials available, let the user log in.
   if not creds or not creds.valid:
       if creds and creds.expired and creds.refresh_token:
           creds.refresh(Request())
       else:
           flow = InstalledAppFlow.from_client_secrets_file(
               CREDENTIALS_FILE, SCOPES)
           creds = flow.run_local_server(port=0)

       # Save the credentials for the next run
       with open('token.pickle', 'wb') as token:
           pickle.dump(creds, token)

   service = build('calendar', 'v3', credentials=creds)
   return service   



a=str(get_calendar_service()).lstrip("Please visit this URL to authorize this application: ")
print(a)