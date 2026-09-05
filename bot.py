import sys
from pathlib import Path

# Add root directory to Python path to fix ModuleNotFoundError for plugins
sys.path.append(str(Path(__file__).resolve().parent))

from datetime import datetime

from pyrogram import Client
from pyrogram.enums import ParseMode
from pyromod import listen

from config import (
    API_ID,
    API_HASH,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
    OWNER_ID,
    LOGGER
)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_id=API_ID,
            api_hash=API_HASH,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )

        self.LOGGER = LOGGER

    async def start(self):
        await super().start()

        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        self.set_parse_mode(ParseMode.HTML)

        self.LOGGER(__name__).info(
            f"Bot is Started @{usr_bot_me.username}"
        )

        try:
            await self.send_message(OWNER_ID, text=("<b><blockquote>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ by @PyroSznpai</blockquote></b>"))
        except Exception:
            pass

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

    def run(self):
        """Run the bot."""
        super().run()


if __name__ == "__main__":
    Bot().run()
