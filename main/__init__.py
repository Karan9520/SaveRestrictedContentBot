#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("21494091", default=None, cast=int)
API_HASH = config("3ef0c04398ee56082f090ff1ff058da0", default=None)
BOT_TOKEN = config("7616549969:AAHYTw0TeUB-x5Lm1AAPW3Y7dekiolRo2l8", default=None)
SESSION = config("BQFH-UsAm5RjHyKlIEy4gRTzckevax5TloVdAzRS7x3K1VGc587dxqCdIPbo7HSJYvyhmLptgDWMjJERcQo874stJGVTsOEhucfH0AM7lr1MLanLy5-wh0HfnIOUOUFDYMB9eXfra4LaM9pcv3qulEa3LxOvZSKjmw3sqM0SmPqNjlMJNmK1nCl9rQZeaaxYKrJERBjdyZGctq2SHgcLDa7uoRe4BUg_fuoI5SqLHNlO5Yb0yPvJOFol_Wq4PjGeJ8FSn-gmNTGDaMdRuKO_5_jmIDTA2AkXHbCYpWBKrcvCiNjlwmb_ADc__CQc2-pvLa2itshhWUgGi6vKFNxcNJllD5xnowAAAAG8itH1AA", default=None)
FORCESUB = config("@AwaraSupportTeam", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
