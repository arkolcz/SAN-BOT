import discord  # type: ignore
from discord.ext import tasks  # type: ignore
from timetable import Timetable
from constants import BOT_DEDICATED_CHANNEL_ID
from utils import get_from_dotenv


class Bot(discord.Client):
    def __init__(self):
        super().__init__()
        self.timetable = Timetable()
        self.channel = None

    async def on_ready(self) -> None:
        print(f"Bot started as {self.user}")
        self.sync_san_timetable.start()
        channel_id = int(get_from_dotenv(BOT_DEDICATED_CHANNEL_ID))
        self.channel = self.get_channel(channel_id)

    async def on_message(self, message) -> None:
        if message.author == self.user:
            return

        if message.content == "!plan":
            await self.send_current_timetable()

    @tasks.loop(hours=12, reconnect=True)
    async def sync_san_timetable(self) -> None:
        print("Checking SAN timetable")
        if self.timetable.check_timetable_changes():
            await self.send_current_timetable()

    async def send_current_timetable(self):
        response = self.timetable.get_san_timetable()
        await self.channel.send(response)
