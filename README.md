# send_healthCode_toWechat
当健康码状态变化（出现“核酸已采样”或采样结果出来）后，将截图发送给指定用户（群）。

Send the screenshot to Wechat user/group when the status of health code changes.

# Requirements

## python packages
- wxauto : auto send file/message to Wechat user/group, based on uianimation;
- pyautogui : auto keyboard/mouse operations;
- pytesseract : OCR, recognize characters from the screenshot image;
- unidecode : help pytesseract to find Chinese characters.

## pre-operation
- install tesseract binary;
- create a desktop shortcut of the Wechat health code's app;
- specify your own idle_time, positon of your health code's desktop shortcut and the Wechat user you want to send to (微信文件助手 by default);
- set "open Wechat" shortcut as "Windows + w" (optional, in Wechat>Setting>Shortcut).


# Notice:
When the PC Wechat is closed to hide in the system tray, wxauto can not launch it automatically. You can bypass it with launching the program manually, that's why i set a windows shortcut to start it.
