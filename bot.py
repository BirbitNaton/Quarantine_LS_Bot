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
previous_section = 'start'


@bot.message_handler(commands=['start'])
def welcome(message):
    global previous_section
    previous_section = 'start'
    bot.reply_to(message, 'Hello World!')  # Приветствие, введение для пользователя
    welcome_keyboard = Keyboard(message)
    welcome_keyboard.start_keyboard()


@bot.message_handler(regexp='F.A.Q.')
def faq(message):
    global previous_section
    previous_section = 'start_keyboard()'
    faq_keyboard = Keyboard(message)
    faq_keyboard.faq_button_keyboard()


@bot.message_handler(regexp='В главное меню')
def back_to_main_menu(message):
    global previous_section
    previous_section = 'start'
    main_menu_keyboard = Keyboard(message)
    main_menu_keyboard.start_keyboard()


@bot.message_handler(regexp='Stat')
def statistics(message):
    global previous_section
    previous_section = 'start_keyboard()'
    stat_keyboard = Keyboard(message)
    stat_keyboard.stat_keyboard()


@bot.message_handler(regexp='Назад')
def step_back(message):
    step_back_keyboard = Keyboard(message)
    eval('step_back_keyboard.'+previous_section)


@bot.message_handler(regexp='По России')
def russian_stats(message):
    global previous_section
    previous_section = 'stat_keyboard()'
    russian_stats_keyboard = Keyboard(message)
    russian_stats_keyboard.russia_keyboard()


@bot.message_handler(regexp='По Миру')
def world_stats(message):
    global previous_section
    previous_section = 'stat_keyboard()'
    world_stats_keyboard = Keyboard(message)
    world_stats_keyboard.world_keyboard()


bot.polling(none_stop=True, interval=0)
