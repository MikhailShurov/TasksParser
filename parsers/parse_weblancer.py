import save.saved_links as saved_links
import save.save_system as save_system

import requests
from bs4 import BeautifulSoup

import TelegramClient


class Weblancer:
    def __init__(self, ):
        self.current_links = []
        self.latest_links = saved_links.weblancer_last_tasks
        self.TC = TelegramClient.TelegramClient()

    def parse(self):
        self.current_links = ['https://www.weblancer.net' + link.find("a").get("href") for link in BeautifulSoup(requests.get('https://www.weblancer.net/jobs/python/').text, 'lxml').find_all("div", "col-sm-10")]
        message = '''Нашел новые заказы на weblancer:'''
        for link in self.current_links:
            if link not in self.latest_links:
                message += f'\n\n{link}'

        self.latest_links = self.current_links.copy()
        save_system.save(1, self.latest_links)

        if message != '''Нашел новые заказы на weblancer:''':
            self.TC.send_text_message(message)
