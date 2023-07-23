
import os, random

import discord
from dotenv import load_dotenv

load_dotenv() # loads the .env file so it can now be accessed with os.getenv("var_name")
BOT_TOKEN = os.getenv("BOT_TOKEN")
GUILD_ID = os.getenv("TEST_GUILD_ID")

intents = discord.Intents.all() # gives the bot total control over everything i think
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    # find if connected to the specified guild
    # complex version, might be useful for refrence
    #guild = discord.utils.find(lambda g: g.name == GUILD_ID, client.guilds)
    #guild = discord.utils.get(client.guilds, name=GUILD_ID)
    for guild in client.guilds:
        if guild.id == GUILD_ID:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'yo {member.name}, you just joined {member.guild.name}')

@client.event
async def on_message(message):
    if message.content == 'stop':
        raise discord.DiscordException
    elif message.author == client.user:
        return

    first_three_letters = message.content[0:3].lower()
    if first_three_letters == "i'm" or first_three_letters == "im ":
        response = f"hello {message.content[3:].lower()}, hehehehe"
        await message.channel.send(response)

#keep at end of main
client.run(BOT_TOKEN)
