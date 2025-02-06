import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7994585610:AAGn_SuD_WZYSKE4gpEWS4TAjh7iyi4u6wQ")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22817133"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "65b44989de9accc59c64691b308da0f7")
#Your db channel Id
CHANNEL_ID = os.environ.get("CHANNEL_ID", "-1002454677208")
# NAMA OWNER
OWNER = os.environ.get("OWNER", "DARKXSIDE78")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1136967391"))
#Port
PORT = os.environ.get("PORT", "8000")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Blakite_Ravii:Ravi8962@cluster0.vdv6h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "AutoAnimeFileBot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", "-1002152715889")
FORCE_SUB_CHANNEL2 = os.environ.get("FORCE_SUB_CHANNEL2", "-1002351086184")
FORCE_SUB_CHANNEL3 = os.environ.get("FORCE_SUB_CHANNEL3", "-1002387103614")
FORCE_SUB_CHANNEL4 = os.environ.get("FORCE_SUB_CHANNEL4", "-1002075491702")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "900")) # auto delete in seconds

START_PIC = os.environ.get("START_PIC", "https://wallpapers.com/images/featured/one-piece-desktop-idg4aqn5l0lh40dk.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://www.desktophut.com/images/thumb_1684136393_444810.jpg")

#start messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ʙᴀᴋᴋᴀᴀᴀ!!! {first_name}</b>,\n\n <b>ɪ ᴀᴍ 9ᴀɴɪᴍᴇ ʙᴏᴛ, ɪ ᴀᴍ ᴀɴɪᴍᴇ ᴘʀᴏᴠɪᴅᴇʀ ʙᴏᴛ ᴀɴᴅ ɢᴇᴛ ᴀɴɪᴍᴇ ғʀᴏᴍ ᴍᴇ ʙʏ ᴜsɪɴɢ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "6302971969 2077116559 1785065025 6844586745 6931518311 5983649308 6931518311").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b><i>Please Join Following Channels to Use this Bot!</i></b>")

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
   
