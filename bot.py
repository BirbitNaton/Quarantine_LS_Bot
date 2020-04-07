import telebot
import time

# import logging
# import ssl

from telebot import types

import config
from keyboard import *

from inline_keyboard import *

# from aiohttp import web

API_TOKEN = config.token

Bot = telebot.TeleBot(token=API_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'Hello World!')
    keyboard1 = Keyboard(message)
    keyboard1.start_keyboard()
    print(message)


bot.polling(none_stop=True, interval=0)
