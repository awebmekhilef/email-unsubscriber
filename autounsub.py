#! /usr/bin/env python3

import ezgmail
import webbrowser
import bs4
import re

ezgmail.init()

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
    webbrowser.open(link)
