from pyrogram import Client
from pyromod import listen
from pyrogram.enums import PharseMode

class = Bot(Client):
    def __init__(self):
      super().__init__(
          name="Bot",
          api_id=API_ID,
          api_hash=API_HASH,
          plugins={
            "root"= "plugins"
          },
          workers=TG_BOT_WORKERS,
          bot_token=TG_BOT_TOKEN
      )
      self.LOGGER = LOGGER

async des start(self):
    await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

self.set_parse_mode(ParseMode.HTML)
self.LOGGER(__name__).info("Bot is Started @{self.username}")

 try: await self.send_message(OWNER_ID, text = f"<b><blockquote> Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ by @PyroSznpai</blockquote></b>")
        except: pass

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

    def run(self):
        """Run the bot."""
        super().run()
