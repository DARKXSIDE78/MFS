import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7091109292:AAGVeX5BIEzxKLyWz-iIKs-kYd6ZFAMkchk")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "17417255"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "73d424d9847f968130cd5b41946f7a5d")
#Your db channel Id
CHANNEL_ID = os.environ.get("CHANNEL_ID", "@GenAnimeOngoingCloud")
# NAMA OWNER
OWNER = os.environ.get("OWNER", "DARKXSIDE78")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6039119180"))
#Port
PORT = os.environ.get("PORT", "8000")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://nitinkumardhundhara:DARKXSIDE78@cluster0.wdive.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "PirateAutoAnime")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNELS = [
    chan_id.strip() for chan_id in 
    os.environ.get("FORCE_SUB_CHANNELS", "").split(",")
    if chan_id.strip()
]

BLOCKED_USERS = set()
ACTIVE_USERS = set()
FILES_UPLOADED = 0

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1600")) # auto delete in seconds

START_PIC = os.environ.get("START_PIC", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJIlnX3NgZKMLrKER8AogHGy_lAFQ4xj_dig&s")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRu7BkhIgEktHKikOKaTY1Qh4IUpzxaWkox0A&s")

#start messages
START_MSG = os.environ.get("START_MESSAGE", "<b>Hᴇʟʟᴏ, [{first}]\nɪ ᴀᴍ Sᴀsᴜᴋᴇ Uᴄʜɪʜᴀ.\n\nCʀᴇᴀᴛᴏʀ: <a href='t.me/darkxside78'>ᴅᴀʀᴋxsɪᴅᴇ</a>.</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "6302971969").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>{first}...\nʏᴏᴜ sᴛᴀɴᴅ ʙᴇғᴏʀᴇ ᴘᴏᴡᴇʀ ʙᴇʏᴏɴᴅ ᴄᴏᴍᴘʀᴇʜᴇɴsɪᴏɴ.\nᴊᴏɪɴ ᴍʏ ʟᴏʀᴅ’s ᴄʜᴀɴɴᴇʟ...</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>ɪ sʜᴀʟʟ ɢʀᴀɴᴛ ʏᴏᴜ ᴛʜᴇ ᴍᴇʀᴄʏ ᴏғ sɪʟᴇɴᴄᴇ. sᴘᴇᴀᴋ ɴᴏ ᴍᴏʀᴇ.</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(7086472788)

LOG_FILE_NAME = "bot.txt"

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
   
