import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token)


class Keyboard:
    def __init__(self, message):
        self.message = message

    def start_keyboard(self):
        markup = types.ReplyKeyboardMarkup()
        button1 = types.KeyboardButton(' Simple Keyboard 2')  # \ud83d\udcbc
        button2 = types.KeyboardButton(' Inline Keyboard 2')  # \ud83c\udfe2
        button3 = types.KeyboardButton(' Callback Inline 2')  # \ud83d\udcf2
        # markup.ResizeKeyboard = True
        markup.row(button1, button2)
        markup.row(button3)
        self.send_message = bot.send_message(self.message.from_user.id, 'Text', reply_markup=markup)

    def button_one_keyboard(self, message):
        markup = types.ReplyKeyboardMarkup()
        button1 = types.KeyboardButton('Button 1')
        button2 = types.KeyboardButton('Button 2')
        back_button = types.KeyboardButton('Back to main menu')
        markup.row(button1, button2)
        markup.row(back_button)
        bot.send_message(message.chat.id, 'Keyboard level 2.', reply_markup=markup)
