import os
from random import random
from threading import Thread
from time import sleep
import time
import random
from time import mktime
from pypresence import Presence
import subprocess
import platform
"""
https://discord.com/developers/applications/940028576407912450/rich-presence/assets
"""

while True:
    client_id = '940028576407912450'
    RPC = Presence(client_id)
    RPC.connect()
    start_time=time.time()
    print(RPC.update(state="Launched With Lunar Client QT", details="State: Playing 1.8.9", large_image="large", buttons=[{"label": " My Github", "url": "https://github.com/Briiqn"}]))
    time.sleep(10)
