import os
import pyautogui as pg
import subprocess
import time as t
import pandas as pd
import openpyxl
from config import Config

comment_count = Config.comment_count
end_count = Config.end_count
url = Config.url
excel_path = os.path.join(os.getcwd(),"data.xlsx")
excel_data = pd.read_excel(excel_path, sheet_name='Sheet1')

# Browser location
t.sleep(2)
pg.moveTo(803, 746, duration=0.5)
# Select browser with loaded page
pg.leftClick()
t.sleep(2)


for column in excel_data['Comments'].tolist():
    pg.moveTo(1357, 132, duration=0.5)
    pg.dragTo(1357, 232, button='left', duration=0.5)
    t.sleep(1)
    # select comment
    pg.moveTo(229, 588, duration=0.5)
    pg.leftClick()
    # Write comment in box
    pg.write(str(excel_data['Comments'][comment_count]))
    #pg.press("enter")
    t.sleep(2)
    # Next Track
    pg.moveTo(160, 50, duration=0.5)
    pg.leftClick()
    # next track url
    pg.write(url+str(excel_data['Tracks'][comment_count]))
    pg.press("enter")
    comment_count += 1 
    t.sleep(15)






   