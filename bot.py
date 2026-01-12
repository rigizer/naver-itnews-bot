#-*- coding: utf-8 -*-

import json
import os
import telegram

folder_path = os.path.dirname(os.path.realpath(__file__))
with open(folder_path + "/setting/bot_info.json") as json_file:
    bot_json = json.load(json_file)

naver_bot = bot_json.get("naverItNewsCrawlBot")

tg_token = naver_bot.get("token")
tg_chatid = naver_bot.get("chatId")
tg_bot = telegram.Bot(token=tg_token)

async def send(message):
    await tg_bot.send_message(
        chat_id=tg_chatid,
        text=message,
        disable_web_page_preview=True
    )

async def send_message(title_list, url_list, info_list):
    if len(info_list) == 0:
        for m_index in range(len(title_list)):
            message = title_list[m_index] + "\r\n" + url_list[m_index]
            await send(message)
    else:
        for message in info_list:
            await send(message)