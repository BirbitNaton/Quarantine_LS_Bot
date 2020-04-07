import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token)


class InlineKeyboard:
    def __init__(self, message):
        self.message = message

    def button_two_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Google', url='https://google.com')
        keyboard.add(url_button)
        bot.send_message(self.message.chat.id, 'If you press the button then go to google', reply_markup=keyboard)

    def callback_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text='More', callback_data='callback')
        keyboard.add(button)
        bot.send_message(self.message.chat.id, 'You can use callback inline button in your bot.', reply_markup=keyboard)
