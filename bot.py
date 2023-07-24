# starts the bot
import os, random

import discord
from dotenv import load_dotenv
from discord.ext import commands

# my stuff :)
import JsonManager
from CommandManager import CommandManager
from Command import Command

commandManager = CommandManager()

def getCommandManager():
    return commandManager

def getCommand():
    return Command

load_dotenv() # loads the .env file so it can now be accessed with os.getenv("var_name")

BOT_TOKEN = os.getenv("BOT_TOKEN")
GUILD_ID = os.getenv("TEST_GUILD_ID")


#client = discord.Client(intents=intents)

class YeetBot(discord.Client):
    async def on_ready(self):
        print(f'{self.user.name} has connected.')
        for guild in self.guilds:
            JsonManager.add_new_guild(guild)
    async def on_message(self, message):
        await commandManager.on_message(message)

intents = discord.Intents.all() # gives the bot total control over everything i think
yeet_bot = YeetBot(intents=intents)
yeet_bot.run(BOT_TOKEN)
