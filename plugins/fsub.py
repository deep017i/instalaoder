# © Coded by @Dypixx

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from var import AUTH_CHANNELS, ADMIN
from pyrogram.errors import RPCError
from Script import txt

async def get_fsub(client, message):
    dy = await client.get_me()
    bot = client
    user_id = message.from_user.id
    not_joined = []
    
    for channel_id in AUTH_CHANNELS:
        try:
            member = await bot.get_chat_member(channel_id, user_id)
            if member.status == "kicked":
                await message.reply("**🚫 You are banned from using this bot**",
                                    reply_markup=InlineKeyboardMarkup(
                                        [[InlineKeyboardButton("Support", user_id=int(ADMIN))]]
                                    ))
            if member.status in ["left", "restricted"]:
                not_joined.append(channel_id)
        except RPCError:
            not_joined.append(channel_id)
    
    # If no channels are left to join, return True
    if not not_joined:
        return True
    
    buttons = []
    for index, channel_id in enumerate(not_joined, 1):
        try:
            chat = await bot.get_chat(channel_id)
            channel_link = chat.invite_link
            if not channel_link:
                raise ValueError("No invite link available")
            buttons.append(InlineKeyboardButton(f"🔰 Channel {index} 🔰", url=channel_link))
        except Exception as e:
            print(f"Error fetching channel data: {e}")
    
    # Separate "Try Again" button
    try_again_button = InlineKeyboardButton("🔄 Try Again", url=f"https://t.me/{dy.username}?start=start")
    
    # Now we add the "Try Again" button at the end, but **only once**
    buttons.append(try_again_button)
    
    # Group buttons into rows (2 buttons per row) and make sure the "Try Again" button is in its own row.
    formatted_buttons = [buttons[i:i + 2] for i in range(0, len(buttons) - 1, 2)]  # Group channel buttons in pairs
    
    # Ensure "Try Again" is always placed in a separate row
    formatted_buttons.append([buttons[-1]])  # Add "Try Again" in its own row

    await message.reply(txt.FORCE_SUBSCRIBE_TEXT.format(message.from_user.mention),
                        reply_markup=InlineKeyboardMarkup(formatted_buttons))
    
    return False



# async def get_fsub(client, message):
#     dy = await client.get_me()
#     bot = client
#     user_id = message.from_user.id
#     not_joined = []
#     for channel_id in AUTH_CHANNELS:
#         try:
#             member = await bot.get_chat_member(channel_id, user_id)
#             if member.status == "kicked":
#                 await message.reply("**🚫 You are banned from using this bot**",
#                                     reply_markup=InlineKeyboardMarkup(
#                                         [[InlineKeyboardButton("Support", user_id=int(ADMIN))]]
#                                     ))
#             if member.status in ["left", "restricted"]:
#                 not_joined.append(channel_id)
#         except RPCError:
#             not_joined.append(channel_id)
#     if not not_joined:
#         return True
#     buttons = []
#     for index, channel_id in enumerate(not_joined, 1):
#         try:
#             chat = await bot.get_chat(channel_id)
#             channel_link = chat.invite_link
#             if not channel_link:
#                 raise ValueError("No invite link available")
#             buttons.append(InlineKeyboardButton(f"🔰 Channel {index} 🔰", url=channel_link))
#         except Exception as e:
#             print(f"Error fetching channel data: {e}")
#     try_again_button = InlineKeyboardButton("🔄 Try Again", url=f"https://t.me/{dy.username}?start=start")
#     buttons.append(try_again_button)

#     formatted_buttons = [buttons[i:i + 2] for i in range(0, len(buttons), 2)]
    
#     await message.reply(txt.FORCE_SUBSCRIBE_TEXT.format(message.from_user.mention),
#                         reply_markup=InlineKeyboardMarkup(formatted_buttons))
#     return False

"""
This code is created and owned by @Dypixx. Do not remove or modify the credit.

Removing the credit does not make you a developer; it only shows a lack of respect for real developers.
  
Respect the work. Keep the credit.

"""
