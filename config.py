import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7427556898:AAHuQ3dLGITJyi4fKcmGkyyVfRqp2ler_30")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22902589"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3045f3e99c422584a2b587e0d9731170")
#Your db channel Id
CHANNEL_ID = os.environ.get("CHANNEL_ID", "@HKBMOVIESDatabase")
# NAMA OWNER
OWNER = os.environ.get("OWNER", "DARKXSIDE78")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7385295244"))
#Port
PORT = os.environ.get("PORT", "8020")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb://nitinkumardhundhara:DARKXSIDE78@cluster0.wdive.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "MovieCollab")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", "@AnimePFP_HKB")
#FORCE_SUB_CHANNEL2 = os.environ.get("FORCE_SUB_CHANNEL2", "@HKB_MOVIES")
#FORCE_SUB_CHANNEL3 = os.environ.get("FORCE_SUB_CHANNEL3", None)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "3600")) # auto delete in seconds

START_PIC = os.environ.get("START_PIC", "https://t.me/BatchBotLog/1825")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://t.me/BatchBotLog/1825")

#start messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... <b>{first} ! 💥</b>\n\n ɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ...!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - <a href='https://t.me/hkb_movies'>HKB MOVIES</a></b>")
try:
    ADMINS=[6376328008, 7086472788]
    for x in (os.environ.get("ADMINS", "6019259215").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ʜᴇʟʟᴏ {first}...\nᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>ʙᴀᴋᴋᴀᴀᴀ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!!</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

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
   
