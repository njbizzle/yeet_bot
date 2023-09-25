# starts the bot
import os, random

import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import commands

# my stuff :)
import JsonManager
from Cogs.TestJsonCog import TestJsonCog



load_dotenv() # loads the .env file so it can now be accessed with os.getenv("var_name")

BOT_TOKEN = os.getenv("BOT_TOKEN")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


class YeetBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()  # gives the bot total control over everything i think
        super().__init__(command_prefix='!', intents=intents)
    async def load_cogs(self):
        for filename in os.listdir("./Cogs"):
            if filename.endswith(".py"):
                cog_path = f"Cogs.{filename[:-3]}"
                print(f"added cog: {cog_path}")
                await self.load_extension(cog_path)


    async def on_ready(self):
        print(f'{self.user.name} has connected.')

        await self.load_cogs()
        await self.change_presence(activity=discord.Game("Hollow Knight: Silksong"))

yeet_bot = YeetBot()
yeet_bot.run(BOT_TOKEN)
