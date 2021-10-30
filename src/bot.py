import discord  # type: ignore


class Bot(discord.Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print(f"Bot started as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "?plan":
            response = "Dummy response"
            await message.channel.send(response)
