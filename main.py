from wxauto import *
import os
import time
import pyautogui as pyxx
import datetime
pyxx.PAUSE = 5
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract'
from unidecode import unidecode

idle_time = [(datetime.time(0,0,0),datetime.time(8,0,0)),
             (datetime.time(23,30,0),datetime.time(23,59,59))]

last_status = 'He Suan Yi Cai Yang'

def status_changed(img_name):
    global last_status
    text = unidecode(pytesseract.image_to_string(Image.open(img_name), lang='chi_sim'))
    if last_status in text:
        return False
    else:
        if last_status == "He Suan Yi Cai Yang":
            last_status = ""
        else:
            last_status = "He Suan Yi Cai Yang"
        return True


def wx_send(img_name):
    wx = WeChat()
    wx.GetSessionList()
    who = '文件传输助手'
    wx.ChatWith(who)
    wx.SendFiles(img_name)
    pyxx.hotkey('win', 'm') # minimize all windows


def do_check():
    pyxx.hotkey('alt', 'w') # user-defined shortcut to open wechat
    pyxx.hotkey('win', 'm') # minimize all windows
    pyxx.click(clicks=2, interval=0.25, x=300, y=30) # desktop small app icon location
    pyxx.click(x=962, y=439) # click healthCode
    pyxx.click(x=1166, y=544) # click right to get baby's healthcode
    pyxx.moveTo(1227, 931) # move mouse out of healthCode region

    now = datetime.datetime.now()
    img_name = "{}.png".format(now.strftime("%Y_%m_%d_%H_%M_%S"))
    pyxx.screenshot(img_name, region=(811,194,411,732))
    pyxx.click(x=1197, y=172)
    if status_changed(img_name):    # if status of healthCode changes
        wx_send(img_name)
    else:
        os.remove(img_name)

def check():
    try:
        do_check()
    except Exception as e:
        print(e)

def in_idle_time():
    now = datetime.datetime.now().time()
    for (start, end) in idle_time:
        if start <= now <= end:
            return True
    return False

time.sleep(3)
pyxx.hotkey('win', 'm') # minimize all windows
while 1:
    if in_idle_time():
        check()
    time.sleep(60)  # put in tail for debugging

