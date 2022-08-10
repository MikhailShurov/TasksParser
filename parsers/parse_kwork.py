from selenium.webdriver.common.by import By

import saved_links
import save_system

from time import sleep


class Kwork:
    def __init__(self, browser):
        self.browser = browser

        self.current_links = []
        self.latest_links = saved_links.kwork_last_links

    def parse(self):
        self.current_links = []
        self.browser.get('https://kwork.ru/projects?c=41')
        sleep(10)
        tasks = self.browser.find_elements(By.CSS_SELECTOR, '.want-card')
        message = '''Kwork, новые задания в питоне:
'''
        for task in tasks:
            link = task.find_element(By.TAG_NAME, 'a').get_attribute('href')
            if link not in self.latest_links:
                message += '\n'
                message += link
            self.current_links.append(link)

        self.latest_links = self.current_links.copy()
        save_system.save(2, self.latest_links)

