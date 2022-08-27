#! /usr/bin/env python3

import ezgmail
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import bs4
import re

ezgmail.init()

browser = webdriver.Chrome()

unsub_links = []
unsub_hosts = []
unsub_regex = re.compile('|'.join(['opt(\s|-)?out', 'unsubscribe']), re.IGNORECASE)

num_unsub = 0

# Retrieve all unsubscribe links
for thread in ezgmail.recent(100):
    for message in thread.messages:
        soup = bs4.BeautifulSoup(message.body, 'html.parser')

        for elem in soup.select('a'):
            if unsub_regex.search(elem.text):
                link = elem.get('href')
                host = urlparse(link).netloc

                # If we already have a link to the organization, skip it
                if host in unsub_hosts:
                    continue

                unsub_hosts.append(host)
                unsub_links.append(link)

                num_unsub += 1

# Open the links in the browser
for i, link in enumerate(unsub_links):
    browser.get(link)

    print(f'Unsubscribing from {browser.title} ({unsub_hosts[i]})')

    try:
        # In the case that you need to press a button to unsubscribe
        unsub_btn = browser.find_element(By.CSS_SELECTOR, 'input[type=submit]')
        unsub_btn.click()
    except:
        pass

input(f'Total unsubscriptions: {num_unsub}.\nPlease verify browser tabs. Press enter to exit...')
