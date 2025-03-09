import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON, OWNER_ID
from helper_func import encode

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.user(OWNER_ID) & ~filters.command(['start','users','broadcast','batch','genlink','stats','restart','id','add_admin','remove_admin','add_fsub','remove_fsub','admins','fsub','setdeletetimer']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Pʟᴇᴀsᴇ Wᴀɪᴛ...!", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Sᴏᴍᴇᴛʜɪɴɢ Wᴇɴᴛ Wʀᴏɴɢ...!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    FILES_UPLOADED += 1  # Update stats counter
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Sʜᴀʀᴇ Uʀʟ", url=f'https://telegram.me/share/url?url={link}')]])

    await reply_text.edit(f"<b>Uᴘʟᴏᴀᴅᴇᴅ Sᴜᴄᴄᴇssꜰᴜʟʟʏ</b>\n\n</b>Sʜᴀʀᴇᴀʙʟᴇ Lɪɴᴋ﹕</b>\n\n{link}", reply_markup=reply_markup, disable_web_page_preview = True)

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)

@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Sʜᴀʀᴇ Uʀʟ", url=f'https://telegram.me/share/url?url={link}')]])
    FILES_UPLOADED += 1  # Update stats counter
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
