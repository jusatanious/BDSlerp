import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random
import asyncio

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)#, help_command=None)

#Initilization confirmation
@bot.event
async def on_ready():
    print(f"Bot is ready!, {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!coinflip'):
        i = random.randint(1,2)
        await message.delete()
        if i == 1:
            ans = await message.channel.send("Heads")
        else:
            ans = await message.channel.send("Tails")
        await asyncio.sleep(5)
        await ans.delete()
    
bot.run(token, log_handler=handler, log_level = logging.DEBUG)