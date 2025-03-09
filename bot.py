from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import *

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER
        self.invitelinks = {}  # Store invite links by channel
        self.uptime = None

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # Initialize force sub channels
        self.FORCE_SUB_CHANNELS = []
        for channel in FORCE_SUB_CHANNELS:
            if channel:
                try:
                    chat = await self.get_chat(channel)
                    if not chat.invite_link:
                        await self.export_chat_invite_link(channel.id)
                        chat = await self.get_chat(channel)
                    self.invitelinks[channel] = chat.invite_link
                    self.FORCE_SUB_CHANNELS.append(channel)
                except Exception as e:
                    self.LOGGER.error(f"Error initializing channel {channel}: {e}")
                    sys.exit(1)

        # Database channel check
        try:
            self.db_channel = await self.get_chat(CHANNEL_ID)
            test = await self.send_message(chat_id=self.db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER.error(f"Database channel error: {e}")
            sys.exit(1)

        # Web server setup
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", PORT).start()

        self.LOGGER.info("Bot Started Successfully!")
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot Stopped Successfully!")
