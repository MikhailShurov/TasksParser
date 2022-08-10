import save.saved_links as saved_links
import save.save_system as save_system

import requests
from bs4 import BeautifulSoup

import TelegramClient


class Kwork:
    def __init__(self):
        self.current_links = []
        self.latest_links = saved_links.kwork_last_links
        self.TC = TelegramClient.TelegramClient()

    def parse(self):
        self.current_links = [link.find("a").get("href") + '/view'for link in BeautifulSoup(requests.get('https://kwork.ru/projects?c=41').text, 'lxml').find_all("div", "wants-card__left")]
        message = '''Нашел новые заказы на kwork:'''
        for link in self.current_links:
            if link not in self.latest_links:
                message += f'\n\n{link}'

        self.latest_links = self.current_links.copy()
        save_system.save(2, self.latest_links)

        if message != '''Нашел новые заказы на kwork:''':
            self.TC.send_text_message(message)