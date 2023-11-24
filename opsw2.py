import telegram
import schedule
import time
import asyncio
import pytz
import datetime

#chat_id = "6744550456"
token = "6802394554:AAEn560wF6oRAx0dtdTiWP24cZd-zBht6vs"
bot = telegram.Bot(token = token)
public_chat_name = '@k201912052test'


def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return

    asyncio.get_event_loop().run_until_complete(send(str(now)))

async def send(time):
    await bot.sendMessage(chat_id=public_chat_name, text=time)
    print(f"Sent message: ", time)

schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

