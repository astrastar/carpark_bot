import telebot
import time
import datetime

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


@bot.message_handler(content_types=['text'])
def func1(message):
    while True:
        time.sleep(60)
        if datetime.datetime.now().hour == 12 and datetime.datetime.now().minute == 0:
            bot.send_message(message.chat.id, f'Первичные {len(first)}\nВторичные {len(second)}\n'
                                              f'Контракты {len(contract)}\nВыдачи {len(selling)}')
            first.clear()
            second.clear()
            contract.clear()
            selling.clear()


bot.polling(timeout=60)

