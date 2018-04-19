import requests
import telebot

TOKEN = '552703504:AAHCMzZBxe2wNVkj4ThOQ0onzkMvEGi46oE'

bot = telebot.TeleBot(TOKEN)

first = []
second = []
contract = []
selling = []


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

def final_message():
    return f'Carpark:\nПервичных посещений: {len(first)}\nВторичных посещений: {len(second)}' \
           f'\nКонтрактов: {len(contract)}\nВыдач: {len(selling)}'

final_message()




bot.polling(timeout=60)

# first - Первичное посещение
# second - Вторичное посещение
# contract - Контракт
# selling - Выдача