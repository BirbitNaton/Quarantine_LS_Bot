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
current_section = 'start'


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'Hello World!')  # Приветствие, введение для пользователя
    welcome_keyboard = Keyboard(message)
    welcome_keyboard.start_keyboard()


@bot.message_handler(regexp='F.A.Q.')
def faq(message):
    faq_keyboard = Keyboard(message)
    faq_keyboard.faq_button_keyboard()


@bot.message_handler(regexp='В главное меню')
def back_to_main_menu(message):
    main_menu_keyboard = Keyboard(message)
    main_menu_keyboard.start_keyboard()


bot.polling(none_stop=True, interval=0)
