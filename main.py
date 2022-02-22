import requests
import json
import config
import csv
import telebot
from telebot import types

def getSchedule():


    try:
        response = requests.get(
            'https://kdp.aqnietgroup.com/v1/workplaces/205',
            params={'date_from': '2021-07-01', 'date_to': '2021-07-01'},
            headers={'Authorization': 'Bearer hOnIRtv-QpC84Ri0aZVRbukoxI3Z7iDr'},
        )

        data = response.text

        todos = json.loads(data)

        # dict_keys(['id', 'pharmacy', 'personal_number', 'working_day', 'date_from', 'date_to', 'day_off'])
        for i in todos['items']:
            values = i.values()
            print(values)
            # send_message(values, '555299761')
    except:
        print('aasdf')





def send_message(text: str, chatid):

    token = "908710316:AAFuUs_51f3ykh9gSrAUhq2w-xZpjm68-6A"
    bot = telebot.TeleBot(token)
    bot.send_message(chatid, text)


    ##Отправить документ в телеграм
    #path = "tasks.xls"
    #with open("tasks.xls", "rb") as file:
    #    f = file.read()
    #bot.send_document(chatid, f, "tasks.xls")


    # @bot.message_handler(content_types=["text"])
    # def repeat_all_messages(message):  # Название функции не играет никакой роли
    #     bot.send_message(message.chat.id, message.text)
    #
    # bot.polling()



def GetEmployeeName(table_number):
    try:
        param = {
            "table_number": table_number,
            "pin": "0000"
        }
        headers = {'Authorization': 'Bearer e0xx6ZvwbBacg-PFZnczijW4nCx6i5-r'}
        response = requests.post('http://api.kazanat.com/v1/finger/employees-find', json=param, headers=headers)

        data = response.json()

        print(data['data'])
    except:
        print('Ошибка при получений данных по сотруднику')


#getSchedule()
GetEmployeeName('EUA-515065')

#send_message("Тест из другого модуля", "555299761")