from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, PORT, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4

import asyncio
import aiohttp

URL = "frail-darya-geniusboi07-2c1562c3.koyeb.app/"  # Replace with your koyeb app link...

async def ping():
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(URL) as response:
                    print(f"Pinged server, status: {response.status}")
            except Exception as e:
                print(f"{e}")
            await asyncio.sleep(600)

loop = asyncio.get_event_loop()
loop.create_task(ping())


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bᴏᴛ ᴄᴀɴ'ᴛ Exᴘᴏʀᴛ Iɴᴠɪᴛᴇ ʟɪɴᴋ ꜰʀᴏᴍ Fᴏʀᴄᴇ Sᴜʙ Cʜᴀɴɴᴇʟ﹗")
                self.LOGGER(__name__).warning(f"Pʟᴇᴀsᴇ Dᴏᴜʙʟᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ FORCE-SUB-CHANNEL ᴠᴀʟᴜᴇ ᴀɴᴅ Mᴀᴋᴇ sᴜʀᴇ Bᴏᴛ ɪs Aᴅᴍɪɴ ɪɴ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ Iɴᴠɪᴛᴇ Usᴇʀs ᴠɪᴀ Lɪɴᴋ Pᴇʀᴍɪssɪᴏɴ, Cᴜʀʀᴇɴᴛ Fᴏʀᴄᴇ Sᴜʙ Cʜᴀɴɴᴇʟ Vᴀʟᴜᴇ﹕ {FORCE_SUB_CHANNEL}")
                sys.exit()
                
        if FORCE_SUB_CHANNEL2:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bᴏᴛ ᴄᴀɴ'ᴛ Exᴘᴏʀᴛ Iɴᴠɪᴛᴇ ʟɪɴᴋ ꜰʀᴏᴍ Fᴏʀᴄᴇ Sᴜʙ Cʜᴀɴɴᴇʟ﹗")
                self.LOGGER(__name__).warning(f"Pʟᴇᴀsᴇ Dᴏᴜʙʟᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ FORCE-SUB-CHANNEL ᴠᴀʟᴜᴇ ᴀɴᴅ Mᴀᴋᴇ sᴜʀᴇ Bᴏᴛ ɪs Aᴅᴍɪɴ ɪɴ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ Iɴᴠɪᴛᴇ Usᴇʀs ᴠɪᴀ Lɪɴᴋ Pᴇʀᴍɪssɪᴏɴ, Cᴜʀʀᴇɴᴛ Fᴏʀᴄᴇ Sᴜʙ Cʜᴀɴɴᴇʟ Vᴀʟᴜᴇ﹕ {FORCE_SUB_CHANNEL2}")
                sys.exit()
                
        if FORCE_SUB_CHANNEL3:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL3)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL3)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL3)).invite_link
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bᴏᴛ ᴄᴀɴ'ᴛ Exᴘᴏʀᴛ Iɴᴠɪᴛᴇ ʟɪɴᴋ ꜰʀᴏᴍ Fᴏʀᴄᴇ Sᴜʙ Cʜᴀɴɴᴇʟ﹗")
                self.LOGGER(__name__).warning(f"Pʟᴇᴀsᴇ Dᴏᴜʙʟᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ FORCE-SUB-CHANNEL ᴠᴀʟᴜᴇ ᴀɴᴅ Mᴀᴋᴇ sᴜʀᴇ Bᴏᴛ ɪs Aᴅᴍɪɴ ɪɴ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ Iɴᴠɪᴛᴇ Usᴇʀs ᴠɪᴀ Lɪɴᴋ Pᴇʀᴍɪssɪᴏɴ, Cᴜʀʀᴇɴᴛ Fᴏʀᴄᴇ Sᴜʙ Cʜᴀɴɴᴇʟ Vᴀʟᴜᴇ﹕ {FORCE_SUB_CHANNEL3}")
                sys.exit()
                
        if FORCE_SUB_CHANNEL4:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL4)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL4)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL4)).invite_link
                self.invitelink4 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bᴏᴛ ᴄᴀɴ'ᴛ Exᴘᴏʀᴛ Iɴᴠɪᴛᴇ ʟɪɴᴋ ꜰʀᴏᴍ Fᴏʀᴄᴇ Sᴜʙ Cʜᴀɴɴᴇʟ﹗")
                self.LOGGER(__name__).warning(f"Pʟᴇᴀsᴇ Dᴏᴜʙʟᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ FORCE-SUB-CHANNEL ᴠᴀʟᴜᴇ ᴀɴᴅ Mᴀᴋᴇ sᴜʀᴇ Bᴏᴛ ɪs Aᴅᴍɪɴ ɪɴ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ Iɴᴠɪᴛᴇ Usᴇʀs ᴠɪᴀ Lɪɴᴋ Pᴇʀᴍɪssɪᴏɴ, Cᴜʀʀᴇɴᴛ Fᴏʀᴄᴇ Sᴜʙ Cʜᴀɴɴᴇʟ Vᴀʟᴜᴇ﹕ {FORCE_SUB_CHANNEL4}")
                sys.exit()
                
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Tʜɪs Is ᴀ Tᴇsᴛ Mᴇssᴀɢᴇ")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Mᴀᴋᴇ Sᴜʀᴇ ʙᴏᴛ ɪs Aᴅᴍɪɴ ɪɴ DB Cʜᴀɴɴᴇʟ, ᴀɴᴅ Dᴏᴜʙʟᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ CHANNEL-ID Vᴀʟᴜᴇ, Cᴜʀʀᴇɴᴛ Vᴀʟᴜᴇ {CHANNEL_ID}")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running...")
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Stopped...")
