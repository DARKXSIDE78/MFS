import os, asyncio, humanize
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserNotParticipant
from bot import Bot
from config import *
from helper_func import subscribed, encode, decode, get_messages
from database.db import add_user, del_user, full_userbase, present_user
from pyrogram.types import Message

GenAnime = FILE_AUTO_DELETE
DARKXSIDE78 = GenAnime
file_auto_delete = humanize.naturaldelta(DARKXSIDE78)

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except Exception as e:
            print(f"Error adding user: {e}")
            pass
    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        ids = []
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
                ids = range(start, end + 1) if start <= end else list(range(start, end - 1, -1))
            except Exception as e:
                print(f"Error decoding IDs: {e}")
                return

        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except Exception as e:
                print(f"Error decoding ID: {e}")
                return

        temp_msg = await message.reply("Pʟᴇᴀsᴇ Wᴀɪᴛ...")
        try:
            messages = await get_messages(client, ids)
        except Exception as e:
            await message.reply_text("Sᴏᴍᴇᴛʜɪɴɢ Wᴇɴᴛ Wʀᴏɴɢ...!")
            print(f"Error getting messages: {e}")
            return
        finally:
            await temp_msg.delete()

        genanime_msg = []  # List to keep track of sent messages

        for msg in messages:
            caption = (CUSTOM_CAPTION.format(previouscaption="" if not msg.caption else msg.caption.html, 
                                             filename=msg.document.file_name) if bool(CUSTOM_CAPTION) and bool(msg.document)
                       else ("" if not msg.caption else msg.caption.html))

            reply_markup = msg.reply_markup if DISABLE_CHANNEL_BUTTON else None

            try:
                copied_msg = await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML, 
                                            reply_markup=reply_markup, protect_content=PROTECT_CONTENT)
                genanime_msg.append(copied_msg)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                copied_msg = await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML, 
                                            reply_markup=reply_markup, protect_content=PROTECT_CONTENT)
                genanime_msg.append(copied_msg)
            except Exception as e:
                print(f"Failed to send message: {e}")
                pass

        k = await client.send_message(chat_id=message.from_user.id, 
                                      text=f"<b>⚠️ Wᴀʀɴɪɴɢ ⚠️\n\nTʜᴇsᴇ Fɪʟᴇ Wɪʟʟ Bᴇ Dᴇʟᴇᴛᴇᴅ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ Iɴ 25Mɪɴ. Fᴏʀᴡᴀʀᴅ Tʜᴇsᴇ Mᴇssᴀɢᴇs...!</b>")

        # Schedule the file deletion
        asyncio.create_task(delete_files(genanime_msg, client, k))

        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚡️ ᴅᴏᴍᴀɪɴ", url = "t.me/Anime_x_Nova"),
                    InlineKeyboardButton("🍁 ᴅᴏᴍᴀɪɴ", url = "t.me/Nova_Networks")
                ],
                [
                    InlineKeyboardButton("🛈 ᴀʙᴏᴜᴛ", callback_data = "about"),
                    InlineKeyboardButton("✘ ᴄʟᴏsᴇ", callback_data = "close")
                ]
            ]
        )
        await message.reply_photo(
            photo= START_PIC,
            caption= START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None if not message.from_user.username else '@' + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id
            ),
            reply_markup=reply_markup,
        )
        return

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    if await subscribed(client, message):
        await start_command(client, message)
        return
    
    buttons = []
    row = []
    # Create buttons dynamically
    for i, channel in enumerate(FORCE_SUB_CHANNELS, 1):
        try:
            invite_link = await client.export_chat_invite_link(channel)
            row.append(InlineKeyboardButton(f"Jᴏɪɴ Cʜᴀɴɴᴇʟ {i}", url=invite_link))
            if len(row) == 2:  # 2 buttons per row
                buttons.append(row)
                row = []
        except Exception as e:
            print(f"Error getting invite link for {channel}: {e}")
    
    if row:  # Add remaining buttons if any
        buttons.append(row)
    
    # Add Try Again button
    try:
        parameter = message.command[1]
        buttons.append([InlineKeyboardButton("Tʀʏ Aɢᴀɪɴ", url=f"https://t.me/{client.username}?start={parameter}")])
    except IndexError:
        buttons.append([InlineKeyboardButton("Tʀʏ Aɢᴀɪɴ", url=f"https://t.me/{client.username}?start")])
    
    await message.reply_photo(
        photo=FORCE_PIC,
        caption=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=message.from_user.username,
            mention=message.from_user.mention,
            id=message.from_user.id
        ),
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=f"Pʀᴏᴄᴇssɪɴɢ...")
    users = await full_userbase()
    await msg.edit(f"{len(users)} ᴜsᴇʀs ᴀʀᴇ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ.")

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ Mᴇssᴀɢᴇ... Tʜɪs Mᴀʏ Tᴀᴋᴇ Sᴏᴍᴇ Tɪᴍᴇ</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except Exception as e:
                print(f"Fᴀɪʟᴇᴅ ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴛᴏ {chat_id}: {e}")
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Bʀᴏᴀᴅᴄᴀsᴛ Cᴏᴍᴘʟᴇᴛᴇᴅ</u>

Tᴏᴛᴀʟ Usᴇʀs: <code>{total}</code>
Sᴜᴄᴄᴇssꜰᴜʟ: <code>{successful}</code>
Uɴsᴜᴄᴄᴇssꜰᴜʟ: <code>{unsuccessful}</code>
Bʟᴏᴄᴋᴇᴅ Usᴇʀs: <code>{blocked}</code>
Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛs: <code>{deleted}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(f"Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ As A Rᴇᴘʟʏ Tᴏ Aɴʏ Tᴇʟᴇɢʀᴀᴍ Mᴇssᴀɢᴇ Wɪᴛʜᴏᴜᴛ Aɴʏ Sᴘᴀᴄᴇs.")
        await asyncio.sleep(8)
        await msg.delete()

# Function to handle file deletion
async def delete_files(messages, client, k):
    await asyncio.sleep(FILE_AUTO_DELETE)  # Wait for the duration specified in config.py
    
    for msg in messages:
        try:
            await client.delete_messages(chat_id=msg.chat.id, message_ids=[msg.id])
        except Exception as e:
            print(f"The attempt to delete the media {msg.id} was unsuccessful: {e}")

    # Safeguard against k.command being None or having insufficient parts
    command_part = k.command[1] if k.command and len(k.command) > 1 else None

    if command_part:
        button_url = f"https://t.me/{client.username}?start={command_part}"
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ɢᴇᴛ ғɪʟᴇ ᴀɢᴀɪɴ!", url=button_url)]
            ]
        )
    else:
        keyboard = None

    # Edit message with the button
    await k.edit_text("<b>Yᴏᴜʀ Vɪᴅᴇᴏ / Fɪʟᴇ Is Sᴜᴄᴄᴇssғᴜʟʟʏ Dᴇʟᴇᴛᴇᴅ ✅</b>", reply_markup=keyboard)
