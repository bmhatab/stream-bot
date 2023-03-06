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

for i in range(1, queue_count+1):
    # Move to options
    pg.moveTo(810, 393, duration=0.5)
    # Select options
    t.sleep(1)
    pg.leftClick()

    # Move to queue
    pg.moveTo(782,317, duration=0.5)
    # Select queue
    t.sleep(1)
    pg.leftClick()
    t.sleep(2.5)

# Transition to music play and forwards
pg.moveTo(188, 518, duration=0.5)
t.sleep(2)
pg.leftClick()
t.sleep(1.5)

for i in range(1, forward_count+1):
    # Move to next button
    pg.moveTo(114, 684, duration=0.5)
    # Select forward
    t.sleep(7)
    pg.leftClick()



    

