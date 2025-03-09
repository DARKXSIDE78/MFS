from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMINS, FORCE_SUB_CHANNELS, BLOCKED_USERS, ACTIVE_USERS, FILES_UPLOADED, FILE_AUTO_DELETE
from database.db import full_userbase
from bot import Bot
import time
import asyncio

@Bot.on_message(filters.command("add_admin") & filters.user(ADMINS))
async def add_admin(client: Client, message: Message):
    try:
        _, user = message.text.split()
        if user.startswith("@"):
            user = (await client.get_users(user)).id
        else:
            user = int(user)
        
        if user not in ADMINS:
            ADMINS.append(user)
            await message.reply(f"Successfully added admin {user}")
        else:
            await message.reply("User is already an admin")
    except:
        await message.reply("Invalid format. Use /add_admin user_id_or_username")

@Bot.on_message(filters.command("remove_admin") & filters.user(ADMINS))
async def remove_admin(client: Client, message: Message):
    try:
        _, user = message.text.split()
        if user.startswith("@"):
            user = (await client.get_users(user)).id
        else:
            user = int(user)
        
        if user in ADMINS:
            ADMINS.remove(user)
            await message.reply(f"Successfully removed admin {user}")
        else:
            await message.reply("User is not an admin")
    except:
        await message.reply("Invalid format. Use /remove_admin user_id_or_username")

@Bot.on_message(filters.command("add_fsub") & filters.user(ADMINS))
async def add_fsub(client: Client, message: Message):
    try:
        _, channel = message.text.split()
        FORCE_SUB_CHANNELS.append(channel.strip())
        await message.reply(f"Added force sub channel: {channel}")
    except:
        await message.reply("Invalid format. Use /add_fsub channel_id_or_username")

@Bot.on_message(filters.command("remove_fsub") & filters.user(ADMINS))
async def remove_fsub(client: Client, message: Message):
    try:
        _, channel = message.text.split()
        if channel.strip() in FORCE_SUB_CHANNELS:
            FORCE_SUB_CHANNELS.remove(channel.strip())
            await message.reply(f"Removed force sub channel: {channel}")
        else:
            await message.reply("Channel not in force sub list")
    except:
        await message.reply("Invalid format. Use /remove_fsub channel_id_or_username")

@Bot.on_message(filters.command("fsub") & filters.user(ADMINS))
async def list_fsub(client: Client, message: Message):
    channels = "\n".join([f"{i+1}. {chan}" for i, chan in enumerate(FORCE_SUB_CHANNELS)])
    await message.reply(f"Current Force Sub Channels:\n{channels}")

@Bot.on_message(filters.command("admins") & filters.user(ADMINS))
async def list_admins(client: Client, message: Message):
    admins = "\n".join([f"{i+1}. {admin}" for i, admin in enumerate(ADMINS)])
    await message.reply(f"Current Admins:\n{admins}")

@Bot.on_message(filters.command("setdeletetimer") & filters.user(ADMINS))
async def set_delete_timer(client: Client, message: Message):
    try:
        _, seconds = message.text.split()
        global FILE_AUTO_DELETE
        FILE_AUTO_DELETE = int(seconds)
        await message.reply(f"Auto-delete timer set to {seconds} seconds")
    except:
        await message.reply("Invalid format. Use /setdeletetimer seconds")

@Bot.on_message(filters.command("stats") & filters.user(ADMINS))
async def detailed_stats(client: Client, message: Message):
    total_users = len(await full_userbase())
    active_users = len(ACTIVE_USERS)
    blocked_users = len(BLOCKED_USERS)
    uptime = time.time() - client.uptime
    hours, rem = divmod(uptime, 3600)
    minutes, seconds = divmod(rem, 60)
    
    stats_text = f"""
📊 Bot Statistics:
    
⏰ Uptime: {int(hours)}h {int(minutes)}m {int(seconds)}s
👥 Total Users: {total_users}
🔥 Active Users: {active_users}
🚫 Blocked Users: {blocked_users}
📁 Files Uploaded: {FILES_UPLOADED}
⏳ Auto-Delete Timer: {FILE_AUTO_DELETE} seconds
    """
    
    await message.reply(stats_text)
