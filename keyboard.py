import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token)

previous_section = 'start'


class Keyboard:

    def __init__(self, message):
        self.message = message

    def start_keyboard(self):
        global previous_section
        previous_section = 'start'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        faq_button = types.KeyboardButton('F.A.Q.')
        stat_button = types.KeyboardButton('Stat')
        prof_button = types.KeyboardButton('Профилактика')
        # markup.ResizeKeyboard = True
        markup.row(faq_button, stat_button)
        markup.row(prof_button)
        text = 'Text'  # Объяснение секций выбора
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def faq_button_keyboard(self):
        global previous_section
        previous_section = 'start_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        sick_button = types.KeyboardButton('Заболевание')
        symptoms_button = types.KeyboardButton('Симптомы')
        miscellaneous_button = types.KeyboardButton('Прочее')
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(sick_button, symptoms_button, miscellaneous_button)
        markup.row(back_button, step_back_button)
        text = 'Text'  # Объяснение секций выбора
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def stat_keyboard(self):
        global previous_section
        previous_section = 'start_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        russia_button = types.KeyboardButton('По России')
        world_button = types.KeyboardButton('По миру')
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(russia_button, world_button)
        markup.row(back_button, step_back_button)
        text = 'Выберите раздел статистики.'
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def russia_keyboard(self):
        global previous_section
        previous_section = 'stat_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(back_button, step_back_button)
        text = 'russian stats'
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def world_keyboard(self):
        global previous_section
        previous_section = 'stat_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(back_button, step_back_button)
        text = 'world stats'
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def miscellaneous_keyboard(self):
        global previous_section
        previous_section = 'faq_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(back_button, step_back_button)
        text = 'Miscellaneous'
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)
