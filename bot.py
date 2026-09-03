from pyrogram import Client
from pyromod import listen

class = Bot(Client):
    def __init__(self):
      super().__init__(
          name="Bot",
          api_id=API_ID,
          api_hash=API_HASH,
          plugins={
            "root"= "plugins"
          },
          bot_token=TG_BOT_TOKEN
      )
      self.LOGGER = LOGGER

async des start(self):
    await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

self.set_parse_mode(ParseMode.HTML)
self.LOGGER(__name__).info("
      

