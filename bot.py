from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode, ChatMemberStatus
import sys
from datetime import datetime
from config import *
import logging

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
        self.logger = LOGGER(__name__)
        self.invitelinks = {}  # Store invite links by username/ID
        self.uptime = None
        self.FORCE_SUB_CHANNELS = []

    async def resolve_channel(self, channel_ref):
        """Resolve channel reference to Chat object"""
        try:
            # Try as username first
            if isinstance(channel_ref, str) and channel_ref.startswith("@"):
                return await self.get_chat(channel_ref)
            # Try as integer ID
            return await self.get_chat(int(channel_ref))
        except ValueError:
            # Handle negative IDs stored as strings
            return await self.get_chat(int(channel_ref))

    async def start(self):
        await super().start()
        self.uptime = datetime.now()
        bot_info = await self.get_me()
        self.logger.info(f"Starting bot @{bot_info.username}")

        try:
            # Initialize force sub channels
            for channel_ref in FORCE_SUB_CHANNELS:
                try:
                    chat = await self.resolve_channel(channel_ref)
                    
                    # Check if bot is admin with invite permissions
                    bot_member = await self.get_chat_member(chat.id, bot_info.id)
                    if not bot_member.privileges.can_invite_users:
                        raise Exception(f"Bot is not admin in {chat.title} or lacks invite permissions")

                    # Create invite link if needed
                    if not chat.invite_link:
                        self.logger.info(f"Creating invite link for {chat.title}")
                        await self.export_chat_invite_link(chat.id)
                        chat = await self.resolve_channel(channel_ref)  # Refresh chat info

                    self.invitelinks[channel_ref] = chat.invite_link
                    self.FORCE_SUB_CHANNELS.append(channel_ref)
                    self.logger.info(f"Initialized channel: {chat.title} ({channel_ref})")

                except Exception as e:
                    self.logger.error(f"Failed to initialize channel {channel_ref}: {str(e)}")
                    sys.exit(1)

            # Initialize database channel
            db_chat = await self.resolve_channel(CHANNEL_ID)
            self.db_channel = db_chat
            test_msg = await self.send_message(db_chat.id, "📁 Database connection test")
            await test_msg.delete()
            self.logger.info(f"Database channel set to: {db_chat.title}")

            # Start web server
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", PORT).start()
            self.logger.info(f"Web server started on port {PORT}")

            self.logger.info("Bot started successfully!")
            self.username = bot_info.username

        except Exception as e:
            self.logger.error(f"Startup failed: {str(e)}")
            await self.stop()
            sys.exit(1)

    async def stop(self, *args):
        await super().stop()
        self.logger.info("Bot stopped successfully")
