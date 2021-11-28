import discord  # type: ignore
from discord.ext import tasks  # type: ignore
from timetable import Timetable


class Bot(discord.Client):
    def __init__(self):
        super().__init__()
        self.timetable = Timetable()

    async def on_ready(self) -> None:
        print(f"Bot started as {self.user}")
        self.update_san_timetable.start()

    async def on_message(self, message) -> None:
        if message.author == self.user:
            return

        if message.content == "!plan":
            message = self.timetable.get_san_timetable()
            await message.channel.send(message)

    @tasks.loop(hours=12, reconnect=True)
    async def update_san_timetable(self) -> None:
        print("Checking SAN timetable")
        self.timetable.update_timetable()
