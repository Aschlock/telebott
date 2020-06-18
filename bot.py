import telebot
from telebot import types
bot = telebot.TeleBot('692035197:AAGdK3HGOvsrnkwidaIoWJ38HA9um7G2gmo')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message)
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Сын собаки")
bot.polling(none_stop=True, interval=1)