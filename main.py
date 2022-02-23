import requests
import json
import csv
import telebot
import pandas as pd


def getSchedule():
    # try:
    response = requests.get(
        'https://kdp.aqnietgroup.com/v1/workplaces/205',
        params={'date_from': '2022-02-01', 'date_to': '2022-02-02'},
        headers={'Authorization': 'Bearer hOnIRtv-QpC84Ri0aZVRbukoxI3Z7iDr'},
    )

    data = response.json()
    dict_sample = {}
    # dict_keys(['id', 'pharmacy', 'personal_number', 'working_day', 'date_from', 'date_to', 'day_off'])

    Name_list = []
    working_day_list = []
    date_from_list = []
    date_to_list = []
    day_off = []

    for i in data['items']:
        # values = i.values()
        values = list(i.values())

        Name_list.append(GetEmployeeName(values[2]))
        working_day_list.append(values[3])
        date_from_list.append(values[4])
        date_to_list.append(values[5])
        day_off.append(values[6])



        # print(values)


    df = pd.DataFrame({'Наименование': Name_list,
                       'Дата': working_day_list,
                       'ВремяС': date_from_list,
                       'ВремяПо': date_to_list,
                       'Выходной': day_off
                       })

    #print(df)
    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sh')
    writer.save()
    return


    token = "908710316:AAFuUs_51f3ykh9gSrAUhq2w-xZpjm68-6A"
    bot = telebot.TeleBot(token)
    doc = open(writer, 'rb')
    bot.send_document('555299761', doc)
    doc.close()

def send_message(text: str, chatid, doc =None, writer =None):
    token = "908710316:AAFuUs_51f3ykh9gSrAUhq2w-xZpjm68-6A"
    bot = telebot.TeleBot(token)

    if doc is None:
        bot.send_message(chatid, text)
    else:
        doc = open(writer, 'rb')
        bot.send_document(chatid, doc)
        doc.close()



def GetEmployeeName(table_number):
    try:
        result = ''
        param = {
            "table_number": table_number,
            "pin": "0000"
        }
        headers = {'Authorization': 'Bearer e0xx6ZvwbBacg-PFZnczijW4nCx6i5-r'}
        response = requests.post('http://api.kazanat.com/v1/finger/employees-find', json=param, headers=headers)

        data = response.json()
        if response.status_code == 200:
            result = data['data']['full_name']
            return result
        else:
            print('Ошибка при получений данных по сотруднику в запросе', data, response.status_code, table_number)

    except:
        print('Ошибка при получений данных по сотруднику', data, response.status_code, table_number)

        return result



# print(alaries1)

getSchedule()
#result = GetEmployeeName('EUA-515065')


# send_message("Тест из другого модуля", "555299761")