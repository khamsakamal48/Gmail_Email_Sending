from __future__ import print_function
import httplib2
import pickle
import os.path
from apiclient import discovery
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import auth
def get_labels():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

SCOPES = ['https://mail.google.com/']
authInst = auth.auth(SCOPES)
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
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = discovery.build('gmail', 'v1', credentials=creds)

import send_email

sendInst = send_email.send_email(service)
'''
message = sendInst.create_message_with_attachment('Sender_Name <Sender_Email_address>','Recipient_Email_Address_1,Recipient_Email_Address_2','Subject','Email_Body', 'Email_Attachment_File_Name' )
'''
message = sendInst.create_message('Sender_Name <Sender_Email_address>','Recipient_Email_Address_1,Recipient_Email_Address_2','Subject','Email_Body' )
sendInst.send_message('me',message)
