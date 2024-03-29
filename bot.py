import telebot
import keyboard
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
    bot.reply_to(message, """Привет! Я бот Lomonosov Studio, и я хочу помочь тебе узнать больше о COVID-19.""")
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


@bot.message_handler(regexp='Stat')
def statistics(message):
    stat_keyboard = Keyboard(message)
    stat_keyboard.stat_keyboard()


@bot.message_handler(regexp='Назад')
def step_back(message):
    step_back_keyboard = Keyboard(message)
    eval('step_back_keyboard.'+keyboard.previous_section)
# В каждом методе класса Keyboard в файле keyboard.py (кроме конструктора) идёт перезапись глобальной previous_section,
# при том, на название предыдущей функции, затем eval() компиллирует сконкатенированную строку


@bot.message_handler(regexp='По России')
def russian_stats(message):
    russian_stats_keyboard = Keyboard(message)
    russian_stats_keyboard.russia_keyboard()


@bot.message_handler(regexp='По Миру')
def world_stats(message):
    world_stats_keyboard = Keyboard(message)
    world_stats_keyboard.world_keyboard()


@bot.message_handler(regexp='По Москве')
def moscow_stats(message):
    moscow_stats_keyboard = Keyboard(message)
    moscow_stats_keyboard.moscow_keyboard()


@bot.message_handler(regexp='Прочее')
def miscellaneous(message):
    faq_misc_keyboard = Keyboard(message)
    faq_misc_keyboard.miscellaneous_keyboard()


@bot.message_handler(regexp='Симптомы')
def symptoms(message):
    symptoms_keyboard = Keyboard(message)
    symptoms_keyboard.symptoms_keyboard()


@bot.message_handler(regexp='Заболевание')
def illness(message):
    illness_keyboard = Keyboard(message)
    illness_keyboard.illness_keyboard()


@bot.message_handler(regexp='Профилактика')
def prophylaxis(message):
    prophylaxis_keyboard = Keyboard(message)
    prophylaxis_keyboard.prophylaxis_keyboard()


bot.polling(none_stop=True, interval=0)
