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
current_section = 'start_keyboard()'


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'Hello World!')  # Приветствие, введение для пользователя
    welcome_keyboard = Keyboard(message)
    welcome_keyboard.start_keyboard()


@bot.message_handler(regexp='F.A.Q.')
def faq(message):
    global current_section
    
    current_section = 'faq_button_keyboard()'
    faq_keyboard = Keyboard(message)
    faq_keyboard.faq_button_keyboard()


@bot.message_handler(redexp='Назад')
def one_layer_back(message):
    global current_section
    
    back_keyboard = Keyboard(message)
    eval('back_keyboard.' + current_section)


bot.polling(none_stop=True, interval=0)
