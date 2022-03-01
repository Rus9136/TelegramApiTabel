import requests
import telebot
import pandas as pd
from datetime import datetime, date, timedelta
import os
import numpy as np

def getSchedule(date_from, date_to, pharmacy, chatid):
    # try:
    response = requests.get(
        'https://kdp.aqnietgroup.com/v1/workplaces/' + pharmacy,
        params={'date_from': date_from, 'date_to': date_to},
        headers={'Authorization': 'Bearer hOnIRtv-QpC84Ri0aZVRbukoxI3Z7iDr'},
    )


    data = response.json()
    Name_list = []
    working_day_list = []
    date_from_list = []
    date_to_list = []
    day_off = []


    if response.status_code != 200:
        print(response.status_code)
        print(data)
        print(date_from)
        print(date_to)
        print(pharmacy)
        print(chatid)
        return

    for i in data['items']:
        # values = i.values()
        values = list(i.values())
        name_personal = GetEmployeeName(values[2])
        if name_personal == '':
            Name_list.append(values[2])
        else:
            Name_list.append(name_personal)

        if values[6] == 1:
            day_off.append('Да')
        else:
            day_off.append('Нет')

        date_time_obj_from = datetime.strptime(values[4], '%Y-%m-%d %H:%M:%S')
        date_time_obj_to = datetime.strptime(values[5], '%Y-%m-%d %H:%M:%S')

        working_day_list.append(values[3])
        date_from_list.append(date_time_obj_from.time())
        date_to_list.append(date_time_obj_to.time())


    df = pd.DataFrame({'Наименование': Name_list, 'Дата': working_day_list, 'ВремяС': date_from_list, 'ВремяПо': date_to_list, 'Выходной': day_off })

    writer = pd.ExcelWriter('График работы.xlsx', engine='xlsxwriter', datetime_format='mmm d yyyy hh:mm:ss')
    df.to_excel(writer, sheet_name='График')

    writer.save()
    send_telegram('', chatid, writer)




def send_telegram(text: str, chatid: str, writer=None):
    token = "908710316:AAFuUs_51f3ykh9gSrAUhq2w-xZpjm68-6A"
    bot = telebot.TeleBot(token)

    if writer is None:
        bot.send_message(chatid, text)
    else:
        doc = open(writer, 'rb')
        bot.send_document(chatid, doc)
        doc.close()
        print('success true')

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
            print('Personal was not found', data, response.status_code, table_number)

    except:
        #print("Сотрудник не найден", data, response.status_code, table_number)
        return result

def getIdNumber():
    result = {'42': '555299761',
            '7': '-697703530',
            '10': '-787351019',
            '108': '-662054159',
            '110': '-603086419',
            '38': '-691703530'}

    df = pd.read_excel('Группы.xlsx')

    for row in df.itertuples(index=False):
        print(row[4])
        break


    return result.items()


def sending():
    df = pd.read_excel('Группы.xlsx')
    for row in df.itertuples(index=False):

        if not np.isnan(row[3]) and not np.isnan(row[4]):
            chatid = round(row[3])
            pharmacy = round(row[4])
            #chatid = 555299761 мой id  в телеграмм




            if date.today().isoweekday() == 2:
                date_from = date.today()
                date_to = date_from - timedelta(days=27)
                getSchedule(str(date_to), str(date_from), str(252), str(-638074373))
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'График работы.xlsx')
                os.remove(path)
                print(pharmacy)
                break


    # if date.today().isoweekday() == 5:
    #     date_from = date.today()
    #     date_to = date_from - timedelta(days=28)
    #     items = getIdNumber()
    #
    #     for i in items:
    #         pharmacy = i[0]
    #         chatid = i[1]
    #         getSchedule(str(date_to), str(date_from), pharmacy, chatid)
    #         path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'График работы.xlsx')
    #         os.remove(path)
    #         break


#getSchedule('555299761')



sending()


#send_telegram('hi','-638074373')


#cols = [4]
#usecols=cols







#print(excel_data_df)

# a = date(2015, 3, 19)
# b = time(2, 10, 43)
# c = datetime.combine(a, b)
#
# print(datetime.time(c))

#result = GetEmployeeName('EUA-515065')


# send_message("Тест из другого модуля", "555299761")
#values = '2022-02-01 09:00:00'
#values = '2018-06-29 08:15:27'
#values2 = '2022-02-01'
# print(values.reverse())
#deadline = datetime.strptime("00:02:02", "%H:%M.%S")


# date_time_str = '2018-06-29 08:15:27'
# date_time_obj = datetime.strptime(values, '%Y-%m-%d %H:%M:%S')
#
# print(date_time_obj.time())
# '2017-04-05-00.11.20'
# today = date.today()
# print(today.year)
# print(today.month)
# print(today.day)
# print(today)


#print(today)
#print(today.strftime("%m/%d/%Y"))  # '04/05/2017'

#print(today.strftime("%Y-%m-%d-%H.%M.%S"))  # 2017-04-05-00.18.00

#deadline = datetime.strptime("%Y-%m-%d-%H.%M", values)
#print(type(deadline), deadline)
