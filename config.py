import os
from os import environ, getenv
import logging
from dotenv import load_dotenv

load_dotenv()
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", 12345678))
API_HASH = os.environ.get("API_HASH", "")

OWNER_ID = int(os.environ.get("OWNER_ID", 12345678))
ADMIN_ID = int(os.environ.get("ADMIN_ID", 12345678))

DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DB_NAME", "animelist")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "150"))

if not TG_BOT_TOKEN:
    logging.warning("TG_BOT_TOKEN is not set!")

if API_ID == 12345678 or not API_ID:
    logging.warning("API_ID is not set!")

if not API_HASH:
    logging.warning("API_HASH is not set!")

if not DB_URI:
    logging.warning("DATABASE_URL is not set!")

START_MSG = os.environ.get("START_MSG", "HAI I AM ANIME LIST BOT")
START_IMG = os.environ.get("START_IMG", "https://graph.org/file/0591ce5558c3ec8fe7612-263292508134daf3e1.jpg")

BOT_STATS_TEXT = "<b>ᴍʏ ᴜᴘᴛɪᴍᴇ ʜᴇʜᴇ~</b>\n{uptime}"
USER_REPLY_TEXT = "<b>ᴡʜᴏ ᴛᴏʟᴅ ʏᴏᴜ ᴛᴏ ᴄᴀʟʟ ᴍᴇ? ʙᴀᴋᴀ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!! 🙄</b>"
USER_ROAST_TEXT = "<b>ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ ᴛᴏ ʙᴀɴ ᴀɴʏᴏɴᴇ, ʏᴏᴜ ᴄʟᴜᴍꜱʏ ᴍᴏʀᴛᴀʟ? ᴋɴᴏᴡ ʏᴏᴜʀ ᴘʟᴀᴄᴇ ꜰɪʀꜱᴛ! 💅</b>"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
