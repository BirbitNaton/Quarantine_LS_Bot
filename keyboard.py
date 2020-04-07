import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token)


class Keyboard:
    def __init__(self, message):
        self.message = message

    def start_keyboard(self):
        markup = types.ReplyKeyboardMarkup()
        faq_button = types.KeyboardButton(text = 'F.A.Q.')
        stat_button = types.KeyboardButton('Stat')
        prof_button = types.KeyboardButton('Профилактика')
        # markup.ResizeKeyboard = True
        markup.row(faq_button, stat_button)
        markup.row(prof_button)
        text = 'Text'  # Объяснение секций выбора
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def faq_button_keyboard(self, message):
        markup = types.ReplyKeyboardMarkup()
        sick_button = types.KeyboardButton('Заболевание')
        symptomes_button = types.KeyboardButton('Симптомы')
        back_button = types.KeyboardButton('Назад')
        markup.row(sick_button, symptomes_button)
        markup.row(back_button)
        text = 'Text'  # Объяснение секций выбора
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)
        
