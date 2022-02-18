import requests
import json
import csv
import telebot
from telebot import types

def getTabel():
    headers = {'Authorization': 'Bearer hOnIRtv-QpC84Ri0aZVRbukoxI3Z7iDr'}
    payload = {'date_from': '2021-07-01', 'date_to': '2021-07-01'}

    response = requests.get(
        'https://kdp.aqnietgroup.com/v1/workplaces/205',
        params={'date_from': '2021-07-01', 'date_to': '2021-07-01'},
        headers={'Authorization': 'Bearer hOnIRtv-QpC84Ri0aZVRbukoxI3Z7iDr'},
    )
    print(response.status_code)

    data = response.text

    todos = json.loads(data)

    # dict_keys(['id', 'pharmacy', 'personal_number', 'working_day', 'date_from', 'date_to', 'day_off'])
    for i in todos['items']:
        # print(i.keys())
        print(i.values())
        # print(i)

    # print(type(todos)) # <class 'list'>

def send_telegram(text: str, chatid):
    token = "hOnIRtv-QpC84Ri0aZVRbukoxI3Z7iDr"

    bot_message = text

    bot_token = token
    bot_chatID = chatid
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    print(response.status_code)




send_telegram("ПРивет это бот из Python", "555299761")