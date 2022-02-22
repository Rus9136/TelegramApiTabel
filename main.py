import requests
import json
import csv
import telebot
import pandas as pd


def getSchedule():

    try:
        response = requests.get(
            'https://kdp.aqnietgroup.com/v1/workplaces/205',
            params={'date_from': '2021-07-01', 'date_to': '2021-07-02'},
            headers={'Authorization': 'Bearer hOnIRtv-QpC84Ri0aZVRbukoxI3Z7iDr'},
        )

        data = response.json()
        dict_sample = {}
        # dict_keys(['id', 'pharmacy', 'personal_number', 'working_day', 'date_from', 'date_to', 'day_off'])

        Name_list = []
        working_day_list =[]
        date_from_list = []
        date_to_list = []
        day_off = []

        for i in data['items']:
            #values = i.values()
            values = list(i.values())

            Name_list.append(values[2])
            working_day_list.append(values[3])
            date_from_list.append(values[4])
            date_to_list.append(values[5])
            day_off.append(values[6])

            #print(values)


        alaries1 = pd.DataFrame({'Name': Name_list,
                                 'working_day': working_day_list,
                                 'date_from': date_from_list,
                                 'date_to': date_to_list,
                                 'day_off': day_off,
                                 })
        print(alaries1)



         # send_message(values, '555299761')
    except:
        print('Ошибка основного запроса')



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


alaries1 = pd.DataFrame({'Name': ['L. Messi', 'Cristiano Ronaldo', 'J. Oblak'],
                                     'Salary': [560000, 220000, 125000]})
#print(alaries1)

getSchedule()
#GetEmployeeName('EUA-515065')

#send_message("Тест из другого модуля", "555299761")