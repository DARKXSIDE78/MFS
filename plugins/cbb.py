from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = (
    "<b>○ Oᴡɴᴇʀ: <a href='https://t.me/jas_mehra'>Jᴀs Mᴇʜʀᴀ</a>\n"
    "○ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/downloads/'>Pʏᴛʜᴏɴ</a>\n"
    "○ Lɪʙʀᴀʀʏ: <a href='https://github.com/pyrogram/pyrogram'>Pʏʀᴏɢʀᴀᴍ</a>\n"
),
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ʙᴀᴄᴋ', callback_data = "back")
                    ]
                ]
            )
        )
    elif data == "back":
        await query.message.edit_reply_markup(
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️ Dᴏᴍᴀɪɴ", url= "https://t.me/Anime_x_Nova"),
                    ],
                    [
                    InlineKeyboardButton("🛈 ᴀʙᴏᴜᴛ", callback_data = "about"),
                    InlineKeyboardButton("✘ ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
