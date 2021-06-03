#-*- coding: utf-8 -*-

import json
import os
import telegram         # pip install python-telegram-bot

folder_path = os.path.dirname(os.path.realpath(__file__))
with open(folder_path + "/setting/bot_info.json") as json_file:
    bot_json = json.load(json_file)

naver_bot = bot_json.get("naverItNewsCrawlBot")

tg_token = naver_bot.get("token")
tg_chatid = naver_bot.get("chatId")
tg_bot = telegram.Bot(token = tg_token)

def send(message):
    tg_bot.sendMessage(chat_id=tg_chatid, text=message)

def send_message(title_list, url_list, info_list):
    if len(info_list) == 0:         # 정상수집의 경우
        for m_index in range(0, len(title_list)):
            message = title_list[m_index] + "\r\n" + url_list[m_index]
            send(message)
    else:                           # 오류 메세지가 있는 경우
        for message in info_list:
            send(message)