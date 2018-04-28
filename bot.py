import requests
import telebot
from telebot import types

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
# @bot.message_handler(commands=['first', 'second', 'contract', 'selling'])
# def command_handler(message):
#     bot.reply_to(message, 'Принято')
#     if 'first' in message.text:
#         first.append(1)
#         print(len(first))
#     elif 'second' in message.text:
#         second.append(1)
#         return len(second)
#     elif 'contract' in message.text:
#         contract.append(1)
#         return len(contract)
#     elif 'selling' in message.text:
#         selling.append(1)
#         return len(contract)
#
# def final_message():
#     return f'Carpark:\nПервичных посещений: {len(first)}\nВторичных посещений: {len(second)}' \
#            f'\nКонтрактов: {len(contract)}\nВыдач: {len(selling)}'
#

@bot.message_handler(commands=['final'])
def foo(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Button_one', callback_data='Number_one')
    key.add(but_1)
    bot.send_message(message.chat.id, 'Select command', reply_markup=key)





bot.polling(timeout=60)

# first - Первичное посещение
# second - Вторичное посещение
# contract - Контракт
# selling - Выдача