#! /usr/bin/env python3

import ezgmail
import bs4
import re

ezgmail.init()

unsub_links = []
unsub_regex = re.compile('|'.join(['opt-out', 'unsubscribe']), re.IGNORECASE)

for thread in ezgmail.recent(5):
    for message in thread.messages:
        soup = bs4.BeautifulSoup(message.body, 'html.parser')

        for elem in soup.select('a'):
            if unsub_regex.search(elem.text):
                unsub_links.append(elem.get('href'))

for link in unsub_links:
    print(link)