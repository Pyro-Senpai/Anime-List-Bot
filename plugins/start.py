import asyncio
import os
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from bot import Bot
from config import START_MSG, START_IMG, BOT_STATS_TEXT
from plugins.PyroSenpai import check_owner_or_admin

@Bot.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    user_first_name = message.from_user.first_name
    mention = message.from_user.mention

    replay_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("About", callback_data="about"),
             InlineKeyboardButton("Help", callback_data="help")],
            [InlineKeyboardButton("Close", callback_data="close")]
        ]
    )
         
    caption = config.START_MSG.format(
        mention=mention, 
        username=username, 
        user_first_name=user_first_name
    )

    await message.reply_photo(
        photo=config.START_IMG,
        caption=caption,
        reply_markup=replay_markup,
        parse_mode=ParseMode.HTML,
        message_effect_id=5104841245755180586)

    return
