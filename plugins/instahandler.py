# © Coded by @Dypixx

from pyrogram import Client, filters
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatAction
from var import IS_FSUB, ADMIN, CHNL_LINK, DUMP_CHANNEL
from .fsub import get_fsub
from .db import dy
from pyrogram import enums

@Client.on_message(filters.text & filters.private)
async def download_instagram_content(client, message):
    if message.text.startswith("/"): return
    if await dy.is_user_banned(message.from_user.id):
        await message.reply("**🚫 Yᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ғʀᴏᴍ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ.**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🧑‍💻 Sᴜᴘᴘᴏʀᴛ', user_id=int(ADMIN))]]))
        return
    if IS_FSUB and not await get_fsub(client, message): return
    url = message.text.strip()
    if not url.startswith("https://www.instagram.com/"):
        await message.reply("**Pʟᴇᴀsᴇ sᴇɴᴅ ᴀ ᴠᴀʟɪᴅ Iɴsᴛᴀɢʀᴀᴍ ᴘᴏsᴛ/ʀᴇᴇʟ ʟɪɴᴋ 🤡**")
        return
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    P=await message.reply("**⏳ Pʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ ʀᴇᴏ̨ᴜᴇsᴛ...**")
    link = f"https://insta-dl.hazex.workers.dev/?url={url}" # API Credit: @MrHazex
    response = requests.get(link)
    if response.status_code != 200:
        await P.edit("**⚠️ Oᴏᴘs! Uɴᴀʙʟᴇ ᴛᴏ ᴘʀᴏᴄᴇss ᴛʜᴇ URL.\nPʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.**")
        return
    data = response.json()
    if not data.get("error") and "result" in data:
        result = data["result"]
        download_url = result["url"]
        extension = result["extension"]
        duration = result["duration"]
        quality = result["quality"]
        Size = result["formattedSize"]
        BTN = InlineKeyboardMarkup([[InlineKeyboardButton("🔗 ⱼₒᵢₙ ₒᵤᵣ 𝄴ₕₐₙₙₑₗ", url=CHNL_LINK)]])
        if extension in ["mp4", "mkv"]:
            await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_VIDEO)
            await client.send_video(DUMP_CHANNEL,video=download_url,caption=f"<b>🎭 Iɴsᴛᴀɢʀᴀᴍ Rᴇᴇʟ Dᴏᴡɴʟᴏᴀᴅᴇᴅ! 🎭\n\n<blockquote>⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}\n📚 Qᴜᴀʟɪᴛʏ: {quality}\n📁 Sɪᴢᴇ: {Size}</blockquote>\n\n📩 Dᴏᴡɴʟᴏᴀᴅᴇᴅ Bʏ: {message.from_user.mention} ({message.from_user.id})</b>",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Close‼️', callback_data='close')]]))
            await message.reply_video(video=download_url,caption=f"<b>🎭 Iɴsᴛᴀɢʀᴀᴍ Rᴇᴇʟ Dᴏᴡɴʟᴏᴀᴅᴇᴅ! 🎭\n\n<blockquote>⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}\n📚 Qᴜᴀʟɪᴛʏ: {quality}\n📁 Sɪᴢᴇ: {Size}</blockquote></b>",reply_markup=BTN)
        elif extension in ["jpg", "jpeg", "png"]:
            await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
            await message.reply_photo(photo=download_url,caption=f"<b>🎭 Iɴsᴛᴀɢʀᴀᴍ Pᴏsᴛ's Dᴏᴡɴʟᴏᴀᴅᴇᴅ! 🎭\n\n<blockquote>📚 Qᴜᴀʟɪᴛʏ: {quality}\n📁 Sɪᴢᴇ: {Size}</blockquote></b>",reply_markup=BTN)
            await client.send_photo(DUMP_CHANNEL,photo=download_url,caption=f"<b>🎭 Iɴsᴛᴀɢʀᴀᴍ Pᴏsᴛ's Dᴏᴡɴʟᴏᴀᴅᴇᴅ! 🎭\n\n<blockquote>📚 Qᴜᴀʟɪᴛʏ: {quality}\n📁 Sɪᴢᴇ: {Size}</blockquote>\n\n📩 Dᴏᴡɴʟᴏᴀᴅᴇᴅ Bʏ: {message.from_user.mention} ({message.from_user.id})</b>",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Close‼️', callback_data='close')]]))
        else:
            await P.edit("**⚠️ Uɴsᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴇᴅɪᴀ ғᴏʀᴍᴀᴛ!**")
            return
        await dy.update_user_activity(message.from_user.id)
        await P.delete()
    else:
        await P.edit("**⚠️ Uɴᴀʙʟᴇ ᴛᴏ ғᴇᴛᴄʜ ᴍᴇᴅɪᴀ.\nPʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ..**")

@Client.on_message(filters.command("insta") & filters.text)
async def download_instagram_content(client, message):
    if message.chat.type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:return await message.reply("**⚠️ Use this command in a group.**")
    if len(message.command) < 2:return await message.reply("**🔗 Provide an Instagram link.**\nExample: `/insta <link>`", quote=True)
    url = message.text.split(None, 1)[1].strip()
    if not url.startswith("https://www.instagram.com/"):return await message.reply("**⚠️ Invalid Instagram link.**")
    if await dy.is_user_banned(message.from_user.id):return await message.reply("**🚫 You're banned.**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Support", user_id=int(ADMIN))]]))
    if IS_FSUB and not await get_fsub(client, message): return
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    P = await message.reply("**⏳ Processing...**")
    link = f"https://insta-dl.hazex.workers.dev/?url={url}"
    response = requests.get(link)
    if response.status_code != 200:
        await P.edit("**⚠️ Oᴏᴘs! Uɴᴀʙʟᴇ ᴛᴏ ᴘʀᴏᴄᴇss ᴛʜᴇ URL.\nPʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.**")
        return
    data = response.json()
    if not data.get("error") and "result" in data:
        result = data["result"]
        download_url = result["url"]
        extension = result["extension"]
        duration = result["duration"]
        quality = result["quality"]
        Size = result["formattedSize"]
        BTN = InlineKeyboardMarkup([[InlineKeyboardButton("🔗 ⱼₒᵢₙ ₒᵤᵣ 𝄴ₕₐₙₙₑₗ", url=CHNL_LINK)]])
        caption_common = f"<b>⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}\n📚 Qᴜᴀʟɪᴛʏ: {quality}\n📁 Sɪᴢᴇ: {Size}</b>"
        if extension in ["mp4", "mkv"]:
            await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_VIDEO)
            await client.send_video(DUMP_CHANNEL, video=download_url, caption=f"<b>🎭 Iɴsᴛᴀ Rᴇᴇʟ</b>\n\n{caption_common}\n\n📩 Bʏ: {message.from_user.mention} ({message.from_user.id})", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Close‼️', callback_data='close')]]))
            await message.reply_video(video=download_url, caption=f"<b>🎭 Iɴsᴛᴀ Rᴇᴇʟ</b>\n\n{caption_common}", reply_markup=BTN)
        elif extension in ["jpg", "jpeg", "png"]:
            await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
            await message.reply_photo(photo=download_url, caption=f"<b>🎭 Iɴsᴛᴀ Pᴏsᴛ</b>\n\n{caption_common}", reply_markup=BTN)
            await client.send_photo(DUMP_CHANNEL, photo=download_url, caption=f"<b>🎭 Iɴsᴛᴀ Pᴏsᴛ</b>\n\n{caption_common}\n\n📩 Bʏ: {message.from_user.mention} ({message.from_user.id})", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Close‼️', callback_data='close')]]))
        else:
            await P.edit("**⚠️ Uɴsᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴇᴅɪᴀ ғᴏʀᴍᴀᴛ!**")
            return
        await dy.update_user_activity(message.from_user.id)
        await P.delete()
    else:
        await P.edit("**⚠️ Uɴᴀʙʟᴇ ᴛᴏ ғᴇᴛᴄʜ ᴍᴇᴅɪᴀ.\nPʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ..**")


"""
This code is created and owned by @Dypixx. Do not remove or modify the credit.

Removing the credit does not make you a developer; it only shows a lack of respect for real developers.
  
Respect the work. Keep the credit.

"""
