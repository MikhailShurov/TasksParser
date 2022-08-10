import telebot
import data.data as data


class TelegramClient:
    def __init__(self):
        self.token = data.telegram_bot_token
        self.bot = telebot.TeleBot(self.token)

        self.chat_ids = data.recepient_ids

    def send_text_message(self, message):
        self.bot.send_message(self.chat_ids[0], message)
