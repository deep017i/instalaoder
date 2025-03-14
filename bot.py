#The repo is fully coded and modified by @Dypixx.
#Please do not sell or remove credits.

from pyrogram.client import Client
from var import *

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="reelloader",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"{me.first_name} is started...")
    async def stop(self, *args):
        await super().stop()
        me = await self.get_me()
        print(f"{me.first_name} is stopped...")


Bot().run()
