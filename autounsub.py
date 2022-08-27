#! /usr/bin/env python3

import ezgmail
from selenium import webdriver
from selenium.webdriver.common.by import By
import bs4
import re

ezgmail.init()

browser = webdriver.Chrome()

unsub_links = []
unsub_regex = re.compile('|'.join(['opt(\s|-)?out', 'unsubscribe']), re.IGNORECASE)

# Retrieve all unsubscribe links
for thread in ezgmail.recent(5):
    for message in thread.messages:
        soup = bs4.BeautifulSoup(message.body, 'html.parser')

        for elem in soup.select('a'):
            if unsub_regex.search(elem.text):
                unsub_links.append(elem.get('href'))

# Open the links in the browser
for link in unsub_links:
    browser.get(link)

    try:
        # In the case that you need to press a button to unsubscribe
        unsub_btn = browser.find_element(By.CSS_SELECTOR, 'input[type=submit]')
        unsub_btn.click()
    except:
        pass
