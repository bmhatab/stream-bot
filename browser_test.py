import os
import pyautogui as pg
import subprocess
import time as t
import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get("https://www.google.com")
t.sleep(2)

# Get the currently active window
active_window = pg.getActiveWindow()
t.sleep(2)

# Get the right bottom to resize
x, y = active_window.right, active_window.bottom
pg.moveTo(x-1, y-1, duration=0.5)
t.sleep(2)

# Drag the object to the top-left corner of the screen (0, 0)
pg.dragTo(815, 555, button='left', duration=0.5)
t.sleep(2)
print(x,y)

# Get the current x and y coordinates of the window
x, y = active_window.left, active_window.top

#Move the window to the top-left corner of the screen (0, 0)
pg.moveTo(x, y, duration=0.5)
t.sleep(1)

# Drag the object to the top-left corner of the screen (0, 0)
pg.dragTo(1, 1, button='left', duration=0.5)
t.sleep(2)
print(x,y)