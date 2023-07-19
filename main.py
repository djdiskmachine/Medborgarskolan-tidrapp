from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import json

def get_value_from_key(input):
    result = []
    for i in lastResponse['answers'][input]['textAnswers']['answers']:
        result.append(i['value'])
    return result

def get_last_response():
    for i in result['responses']:
        if i['responseId'] not in prev_response_ids:
            prev_response_ids.append(i['responseId'])
            return i

Q_DATE = "3c16edf2"
Q_PARTICIPANT = "5c529686"
Q_PLAN = "0f3196bb"
Q_LEARNED = "63f7a573"
Q_LOCATION = "5226eaad"

FORM_ID = '1jo4wmfv_XhQHPnShd1N5WntGlUlD1EdFxngWeM7dHyk'
SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

prev_response_ids = ["ACYDBNgYpFU0FeQ8tb58jKMVhpmlbbfmUD_yXtkvMmXS_PiUup7PId2bubD6jzybDw-rBa4", "ACYDBNjn_Pga1FjcF3gxpJBgA1i98v_ZspVfT_mYnATQ6n6lx3OgQMEzORo2ot4LzEB-s4o", "ACYDBNjegqJ9P6EKR9ZMMqvyZelLYPNMntsqD0FDwxL60CwK2XkaMMvxw9pREoUFrF1kexk"]


store = file.Storage('token.json')
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = discovery.build('forms', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

# Prints the responses of your specified form:
result = service.forms().responses().list(formId=FORM_ID).execute()
# print(">>>All results")
# print(result)

# Get last response in form
lastResponse = get_last_response()

# Get date
participant = get_value_from_key(Q_DATE)
print(participant)

# Get participants
participant = get_value_from_key(Q_PARTICIPANT)
print(participant)

# Get plan
participant = get_value_from_key(Q_PLAN)
print(participant)

# Get learned
participant = get_value_from_key(Q_LEARNED)
print(participant)

# Get location
location = get_value_from_key(Q_LOCATION)
print(location)