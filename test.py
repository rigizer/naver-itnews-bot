import json
import os
import telegram
import asyncio

folder_path = os.path.dirname(os.path.realpath(__file__))
with open(folder_path + "/setting/bot_info.json") as json_file:
    bot_json = json.load(json_file)

naver_bot = bot_json.get("naverItNewsCrawlBot")

tg_token = naver_bot.get("token")
tg_chatid = naver_bot.get("chatId")
tg_bot = telegram.Bot(token = tg_token)

async def send(message):
    await tg_bot.sendMessage(chat_id=tg_chatid, text=message)

if __name__ == "__main__":
    asyncio.run(send("메세지 테스트"))