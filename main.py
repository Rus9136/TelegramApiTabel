import requests
import telebot
import pandas as pd
import datetime
from datetime import datetime, date, time

def getSchedule():
    # try:
    date_from = '2022-01-01'
    date_to = '2022-01-03'
    number = str(110)
    response = requests.get(
        'https://kdp.aqnietgroup.com/v1/workplaces/' + number,
        params={'date_from': date_from, 'date_to': date_to},
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


        #datetime.time


        # print(values)

    df = pd.DataFrame({'Наименование': Name_list,
                       'Дата': working_day_list,
                       'ВремяС': date_from_list,
                       'ВремяПо': date_to_list,
                       'Выходной': day_off
                       })

    #print(df)
    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter', datetime_format='mmm d yyyy hh:mm:ss')
    df.to_excel(writer, sheet_name='ГрафикРаботы')
    writer.save()

    ##Отправка документа в телеграм
    # token = "908710316:AAFuUs_51f3ykh9gSrAUhq2w-xZpjm68-6A"
    # bot = telebot.TeleBot(token)
    # doc = open(writer, 'rb')
    # bot.send_document('555299761', doc)
    # doc.close()

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
            print('Personal was not found', data, response.status_code, table_number)

    except:
        print("Сотрудник не найден", data, response.status_code, table_number)
        return result




#if date.today().isoweekday() == 1:
#    getSchedule()


#getSchedule()

dict = {'52': '-697703530',
        '122': '-697703530',
        '142': '-697703530',
        '38': '-691703530'}

lis = [dict]

for i in dict.items():
    number = i[0]
    id = i[1]
    print(id)



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
