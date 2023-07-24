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


intents = discord.Intents.all() # gives the bot total control over everything i think
yeet_bot = commands.Bot(command_prefix='!', intents=intents)
async def load_cogs():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py"):
            cog_path = f"Cogs.{filename[:-3]}"
            print(f"added cog: {cog_path}")
            await yeet_bot.load_extension(cog_path)
@yeet_bot.event
async def on_ready():
    print(f'{yeet_bot.user.name} has connected.')

    await load_cogs()

    await yeet_bot.change_presence(activity=discord.Game("Hollow Knight: Silksong"))

yeet_bot.run(BOT_TOKEN)
