#The repo is fully coded and modified by @Dypixx.
#Please do not sell or remove credits.

import os

API_ID = os.getenv("API_ID", "22532891")
API_HASH = os.getenv("API_HASH", "f2b6b1f0570fe18c8213e64c477a81d2")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7784529867:AAGm_r84wxjk83MQXqg3PRoAwJk5QUmoLdY")
ADMIN = int(os.getenv("ADMIN", "1782834874"))

CHNL_LINK = os.getenv("CHNL_LINK", "https://t.me/DypixxTech")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002147456374"))
DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-1002147456374"))

DB_URI = os.getenv("DB_URI", "mongodb+srv://starcinebot:mkooaa@werdeveloper.vxfam.mongodb.net/?retryWrites=true&w=majority&appName=werdeveloper")
DB_NAME = os.getenv("DB_NAME", "instalaoder")

IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Enable Force Subscribe
AUTH_CHANNEL = int(os.environ.get("AUTH_CHANNEL", "-1002421861644"))

REEL_AUTO_DELETE = int(os.getenv("REEL_AUTO_DELETE", "600")) #10min
