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

#Initilization
bot = commands.Bot(command_prefix='!', intents=intents)#, help_command=None)

#Initilization confirmation
@bot.event
async def on_ready():
    print(f"Bot is ready!, {bot.user.name}")

@bot.event
async def on_message(message):
    lottery = random.randint(1, 100)
    if message.author == bot.user:
        return

    if message.content.startswith('!coinflip'):
        ans = random.choice(['Heads', 'Tails'])
        await message.channel.send(ans)

    if bot.user.mentioned_in(message):
        await message.channel.send(f"{message.author.mention} SUHWOO")
    
    if lottery == 1:
        response = random.choice([
            f"{message.author.mention} sybau 🥀💔 ",
            f"{message.author.mention} FUCK YOU",
            "ts so kevin 🥀",
            "gurt: yo",
            "Justin is the best Valorant player @pogcast",
            "Deez Nutz","amongus","dabs seductively","🫃",":ericlove:",
            "@omykun",":head:"
        ])
        await message.channel.send(response)
    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level = logging.DEBUG)