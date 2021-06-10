# Edgar Barrera / Github: https://github.com/EdgarCastillo101/EdgarCastillo101
# Copyright (c) 2021 Edgar Barrera

import webbrowser
import time
from pykeyboard import PyKeyboard

count = 0
# If used, this program will route your towards my Github lol.
urls = ['https://github.com/EdgarCastillo101/Data-Structures-Algorithms', 'https://github.com/EdgarCastillo101',
        'hhttps://github.com/EdgarCastillo101/Python-Spammer']
k = PyKeyboard()

while count < 100:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(10)
        k.press_keys(['Command', 'W'])
        count = count + 1

else:
    pass
