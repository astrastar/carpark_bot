import requests
import telebot
from telebot import types
import time
import datetime

TOKEN = '552703504:AAHCMzZBxe2wNVkj4ThOQ0onzkMvEGi46oE'

bot = telebot.TeleBot(TOKEN)

first = []
second = []
contract = []
selling = []


# markup = types.ReplyKeyboardMarkup(row_width=2)
# itembtn = types.KeyboardButton('a')
# markup.add(itembtn)
# bot.send_message()
#
@bot.message_handler(commands=['first', 'second', 'contract', 'selling'])
def command_handler(message):
    bot.reply_to(message, 'Принято')
    if 'first' in message.text:
        first.append(1)
    elif 'second' in message.text:
        second.append(1)
    elif 'contract' in message.text:
        contract.append(1)
    elif 'selling' in message.text:
        selling.append(1)


# @bot.message_handler(content_types=['text'])
# def report(message):
#     while True:
#         time.sleep(60)
#         if datetime.datetime.now().minute == 9:
#             bot.send_message(message, 'rrr')
#


@bot.message_handler(content_types=['text'])
def func1(message):
    while True:
        time.sleep(60)
        if datetime.datetime.now().minute == 0:
            bot.send_message(message.chat.id, f'First {len(first)}, second {len(second)}\n'
                                              f'contracts {len(contract)}, sellings {len(selling)}')
            first.clear()
            second.clear()
            contract.clear()
            selling.clear()

# def report():
#     while True:
#         time.sleep(10)
#         if datetime.datetime.now().hour == 12:
#             return bot.send_message(chat_id='1265800', text=f'First {f}, second {s}'
#                                                             f'\ncontracts {c}\nsellings {sell}')


# report()

# def some_msg():
#     bot.send_message(message.chat.id, 'ffff')
#
# while True:
#     time.sleep(60)
#     if datetime.datetime.now().hour == 10 and datetime.datetime.now(). minute == 4:
#         some_msg()

#
# def final_message():
#     return f'Carpark:\nПервичных посещений: {len(first)}\nВторичных посещений: {len(second)}' \
#            f'\nКонтрактов: {len(contract)}\nВыдач: {len(selling)}'
#

# @bot.message_handler(commands=['final'])
# def foo(message):
#     key = types.InlineKeyboardMarkup()
#     but_1 = types.InlineKeyboardButton(text='Button_one', callback_data='Number_one')
#     key.add(but_1)
#     bot.send_message(message.chat.id, 'Select command', reply_markup=key)





bot.polling(timeout=60)

# first - Первичное посещение
# second - Вторичное посещение
# contract - Контракт
# selling - Выдача