import os
import pyautogui as pg
import subprocess
import time as t
import pandas as pd
import openpyxl
from config import Config

queue_count = Config.queue_count
forward_count = Config.forward_count

#excel_path = os.path.join(os.getcwd(),"audiomack/data.xlsx")

# Browser location
t.sleep(2)
pg.moveTo(803, 746, duration=0.5)
# Select browser with loaded page
pg.leftClick()
t.sleep(2)

# Scroll to track
pg.moveTo(1357, 132, duration=0.5)
pg.dragTo(1357, 232, button='left', duration=0.5)
t.sleep(1)

# Play track before loop starts
pg.moveTo(172,581,duration = 0.5)
pg.leftClick()
t.sleep(2)

for i in range(1, queue_count+1):
    # Move to queue
    pg.moveTo(1008,624,duration=0.5)
    t.sleep(0.5)
   # pg.leftClick()
    # Add to queue
    pg.moveTo(1050,547,duration=0.5)
    pg.click(button='left', clicks=10, interval=0.5)
    t.sleep(2)

for i in range(1, forward_count*10):
    # Move to next button
    pg.moveTo(114, 686, duration=0.5)
    # Select forward
    t.sleep(7)
    pg.leftClick()
