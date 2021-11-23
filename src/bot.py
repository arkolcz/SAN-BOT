import discord  # type: ignore
from site_crawler import Crawler
from constants import SAN_SITE_URL


class Bot(discord.Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print(f"Bot started as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "!plan":
            crawler = Crawler(SAN_SITE_URL)
            response = crawler.get_schedule()
            await message.channel.send(response)
