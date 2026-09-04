from datetime import datetime

import asyncio
import os
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from bot import Bot
from config import START_MSG, START_IMG, BOT_STATS_TXET

# Start Command

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
         
    caption = START_MSG.format(
        mention=mention, 
        username=username, 
        user_first_name=user_first_name
    )

    await message.reply_photo(
        photo=START_IMG,
        caption=caption,
        reply_markup=replay_markup,
        parse_mode=ParseMode.HTML,
        message_effect_id=5104841245755180586)

    return

# Bot Uptime

@Bot.on_message(filters.command("stats") & filters.private)
async def stats_command(bot: Bot, message: Message):
    if not await check_admin_or_owner(message):
        return
    uptime = getattr(bot, "uptime", None)
    if not uptime:
        bot.uptime = datetime.now()
        uptime = bot.uptime
    now = datetime.now()
    delta = now - uptime
    uptime_str = get_readable_time(delta.total_seconds())
    if not uptime_str:
        uptime_str = "0s"
    await message.reply(BOT_STATS_TEXT.format(uptime=uptime_str), parse_mode=ParseMode.HTML)
