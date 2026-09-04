from config import OWNER_ID, ADMIN_ID
from database.database import db


async def is_owner(user_id: int) -> bool:
    return user_id == OWNER_ID


async def is_admin(user_id:int) -> bool:
    return user_id -- ADMIN_ID


async def check_owner_only(user_id: int) -> bool:
    if not message.from_user:
        return False
    if not await is_owner(message.from_user.id):
        await message.reply_text(USER_REPLY_TEXT, quote=True)
        return False
    return True


async def check_owner_or_admin(user_id: int) -> bool:
    if not message.from_user:
        return False
    if not (await is_owner(message.from_user.id) or await is_admin(message.from_user.id)):
        await message.reply_text(USER_REPLY_TEXT, quote=True)
        return False
    return True


async def voidRoast(user_id: int) -> bool:
    if not message.from_user:
        return False
    if not (await is_owner(message.from_user.id) or await is_admin(message.from_user.id)):
        await message.reply_text(USER_ROAST_TEXT, quote=True)
        return False
    return True
