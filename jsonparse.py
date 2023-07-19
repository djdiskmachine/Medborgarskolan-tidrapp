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

q_date = "3c16edf2"
q_participant = "5c529686"
q_plan = "0f3196bb"
q_learned = "63f7a573"
q_location = "5226eaad"

prev_response_ids = ["ACYDBNgYpFU0FeQ8tb58jKMVhpmlbbfmUD_yXtkvMmXS_PiUup7PId2bubD6jzybDw-rBa4", "ACYDBNjn_Pga1FjcF3gxpJBgA1i98v_ZspVfT_mYnATQ6n6lx3OgQMEzORo2ot4LzEB-s4o", "ACYDBNjegqJ9P6EKR9ZMMqvyZelLYPNMntsqD0FDwxL60CwK2XkaMMvxw9pREoUFrF1kexk"]
input = '{"responses": [{"responseId": "ACYDBNjn_Pga1FjcF3gxpJBgA1i98v_ZspVfT_mYnATQ6n6lx3OgQMEzORo2ot4LzEB-s4o", "createTime": "2023-07-19T11:17:22.850Z", "lastSubmittedTime": "2023-07-19T11:17:22.850363Z", "answers": {"5c529686": {"questionId": "5c529686", "textAnswers": {"answers": [{"value": "laptopen"}]}}, "0f3196bb": {"questionId": "0f3196bb", "textAnswers": {"answers": [{"value": "Stackoverflow"}]}}, "3c16edf2": {"questionId": "3c16edf2", "textAnswers": {"answers": [{"value": "Testat igen"}]}}}}, {"responseId": "ACYDBNjegqJ9P6EKR9ZMMqvyZelLYPNMntsqD0FDwxL60CwK2XkaMMvxw9pREoUFrF1kexk", "createTime": "2023-07-19T10:22:21.838Z", "lastSubmittedTime": "2023-07-19T10:22:21.838278Z", "answers": {"5c529686": {"questionId": "5c529686", "textAnswers": {"answers": [{"value": "Migsjälv"}]}}, "0f3196bb": {"questionId": "0f3196bb", "textAnswers": {"answers": [{"value": "Google API dokumentation"}]}}, "3c16edf2": {"questionId": "3c16edf2", "textAnswers": {"answers": [{"value": "Testat"}]}}}}, {"responseId": "ACYDBNjzEvAD_VYFyd43mfpZ329PlV6_iiDCWVz7tZOKtLRoGncGsaeROCKgPA8tgEYfujU", "createTime": "2023-07-19T15:29:37.958Z", "lastSubmittedTime": "2023-07-19T15:29:37.958829Z", "answers": {"5226eaad": {"questionId": "5226eaad", "textAnswers": {"answers": [{"value": "Ombord på Öresundståget"}]}}, "63f7a573": {"questionId": "63f7a573", "textAnswers": {"answers": [{"value": "Jag har lärt mig hur jag kan hämta sista inlägget i formuläret samt relevanta fält"}]}}, "5c529686": {"questionId": "5c529686", "textAnswers": {"answers": [{"value": "Markus Kaczmarek"}, {"value": "Bananer"}]}}, "0f3196bb": {"questionId": "0f3196bb", "textAnswers": {"answers": [{"value": "Jag tänkte testa Google Forms API"}]}}, "3c16edf2": {"questionId": "3c16edf2", "textAnswers": {"answers": [{"value": "2023-07-19"}]}}}}, {"responseId": "ACYDBNgYpFU0FeQ8tb58jKMVhpmlbbfmUD_yXtkvMmXS_PiUup7PId2bubD6jzybDw-rBa4", "createTime": "2023-07-19T14:20:44.647Z", "lastSubmittedTime": "2023-07-19T14:20:44.647699Z", "answers": {"5226eaad": {"questionId": "5226eaad", "textAnswers": {"answers": [{"value": "Öresundståg"}]}}, "63f7a573": {"questionId": "63f7a573", "textAnswers": {"answers": [{"value": "Hur man testar api"}]}}, "5c529686": {"questionId": "5c529686", "textAnswers": {"answers": [{"value": "Markus Kaczmarek"}]}}, "0f3196bb": {"questionId": "0f3196bb", "textAnswers": {"answers": [{"value": "Testa API"}]}}, "3c16edf2": {"questionId": "3c16edf2", "textAnswers": {"answers": [{"value": "2023-07-19"}]}}}}]}'
result = json.loads(input)

# Get last response in form
lastResponse = get_last_response()
print(lastResponse)

# Get date
participant = get_value_from_key(q_date)
print(participant)

# Get participants
participant = get_value_from_key(q_participant)
print(participant)

# Get plan
participant = get_value_from_key(q_plan)
print(participant)

# Get learned
participant = get_value_from_key(q_learned)
print(participant)

# Get location
location = get_value_from_key(q_location)
print(location)
