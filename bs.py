import time

import requests
from bs4 import  BeautifulSoup

def cu(code):
    web = requests.get(f'http://www.bgfbestu.com/gift/useguide?&idx=68&barcode={code}')
    soup = BeautifulSoup(web.content, "html.parser")

    list = soup.find_all('td')
    return list[0].get_text(), list[1].get_text()