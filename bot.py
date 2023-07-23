# starts the bot
import os, random

import discord
from dotenv import load_dotenv
from discord.ext import commands

# my stuff :)
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


intents = discord.Intents.all() # gives the bot total control over everything i think
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected.')

@client.event
async def on_message(message):
    await commandManager.on_message(message)

client.run(BOT_TOKEN)
