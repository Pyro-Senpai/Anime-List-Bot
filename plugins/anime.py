from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, CallbackQuery
from config import ADMIN_ID, OWNER_ID
import json
import os

DATA_FILE = "anime_list.json"
ITEMS_PER_PAGE = 10

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"anime": []}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_anime_page(page: int = 0):
    data = load_data()
    anime_list = data.get("anime", [])
    
    if not anime_list:
        return "No anime found in the list.", None
    
    total_items = len(anime_list)
    total_pages = (total_items + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
    
    page = max(0, min(page, total_pages - 1))
    
    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    current_items = anime_list[start:end]
    
    text = f"Anime List (Page {page + 1}/{total_pages}):\n"
    text += "\n".join([f"- {anime}" for anime in current_items])
    
    buttons = []
    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton("⬅️ Prev", callback_data=f"anime_page_{page - 1}"))
    if page < total_pages - 1:
        nav_buttons.append(InlineKeyboardButton("Next ➡️", callback_data=f"anime_page_{page + 1}"))
    
    if nav_buttons:
        buttons.append(nav_buttons)
        
    reply_markup = InlineKeyboardMarkup(buttons) if buttons else None
    return text, reply_markup

@Bot.on_message(filters.command("addanimelist") & filters.user(ADMIN_ID, OWNER_ID))
def add_anime(client: Client, message: Message):
    if len(message.command) < 2:
        message.reply_text("Please provide anime name. Example: /addanimelist Naruto")
        return
    
    anime_name = " ".join(message.command[1:])
    data = load_data()
    data["anime"].append(anime_name)
    save_data(data)
    
    message.reply_text(f"Anime saved successfully! Use /viewanimelist to see the paginated list.")

@Bot.on_message(filters.command("viewanimelist") & filters.user(ADMIN_ID))
def view_anime_list(client, message):
    text, reply_markup = get_anime_page(0)
    bot_username = client.get_me().username
    deep_link = f"https://t.me/{bot_username}?start=animes"
    text += f"\n\nUser Deep Link:\n{deep_link}"
    
    message.reply_text(text, reply_markup=reply_markup)

@Bot.on_callback_query(filters.regex("^anime_page_"))
def paginate_anime(client: Client, callback_query: CallbackQuery):
    page = int(callback_query.data.split("_")[-1])
    text, reply_markup = get_anime_page(page)
    
    callback_query.message.edit_text(text, reply_markup=reply_markup)
    callback_query.answer()

@Bot.on_message(filters.command("start") & filters.regex("animes"))
def start_with_animes(client: Client, message: Message):
    text, reply_markup = get_anime_page(0)
    message.reply_text(text, reply_markup=reply_markup)

@Bot.on_message(filters.command("animes"))
def show_anime(client, message):
    text, reply_markup = get_anime_page(0)
    message.reply_text(text, reply_markup=reply_markup)

app.run()



        
