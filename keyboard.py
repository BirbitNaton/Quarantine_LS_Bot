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
        Text = 'Text'  # Объяснение секций выбора
        bot.send_message(self.message.from_user.id, Text, reply_markup=markup)

    def button_one_keyboard(self, message):
        markup = types.ReplyKeyboardMarkup()
        button1 = types.KeyboardButton('Button 1')
        button2 = types.KeyboardButton('Button 2')
        back_button = types.KeyboardButton('Back to main menu')
        markup.row(button1, button2)
        markup.row(back_button)
        bot.send_message(message.chat.id, 'Keyboard level 2.', reply_markup=markup)
