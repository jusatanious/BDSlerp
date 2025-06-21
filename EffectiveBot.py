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

anger = 0

#Initilization confirmation
@bot.event
async def on_ready():
    print(f"Bot is ready!, {bot.user.name}")

@bot.event
async def on_message(message):
    lottery = random.randint(1, 85)
    if message.author == bot.user:
        return

    if message.content.startswith('!coinflip'):
        ans = random.choice(['Heads', 'Tails'])
        await message.channel.send(ans)

    if bot.user.mentioned_in(message):
        content = message.content.replace(f"<@{bot.user.id}>", "").strip()
        global anger
        if content.lower() == "suhwoo":
            gif = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWN5ZDQ1b2RrNG45b2M4YjUwdm1iYjI5cHVzOXpjbW94NmoxMzNwZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xSM46ernAUN3y/giphy.gif"
            await message.channel.send(f"{gif}")
        if content.lower() == "fuck you" and anger >= 3:
            if anger >= 3:
                gif = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXlmem13M3oyY2cyN20yMG81aTkxeW1wZzNzejR2OGNhYWowZHo0NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/11tTNkNy1SdXGg/giphy.gif"
                anger = 0
                await message.channel.send(f"{gif}")
            else:
                anger += 1
                gif = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmx3OGs1Y3FsZTRhZjF6eGZnNWVzaXJ2cGZrY2U5d2NzczAzd2psbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KzGCAlMiK6hQQ/giphy.gif"
                await message.channel.send(f"{gif}")
        else:
            await message.channel.send(f"{message.author.mention} SUHWOO")
    
    if lottery == 1:
        user2 = await message.guild.fetch_member(90286939487346688)
        response = random.choice([
            f"{message.author.mention} sybau 🥀💔 ",
            f"{message.author.mention} FUCK YOU",
            "ts so kevin 🥀",
            "gurt: yo","amongus","*dabs seductively*","🫃",":ericlove:",
            f"{user2.mention}",":head:","*boots up hearthstone*",
            "I’m on my Deriod cuh 😢💔",
            "I'm not loyal to anyone, i'm a demon",
            "You see this, I really did this, I'm him",
            "My money long, my pockets deep, no pocket watchin in these parts",
            "They must have amnesia because they forgot that I'm him."
        ])
        await message.channel.send(response)
    
    await bot.process_commands(message)

@bot.command()
async def forcewin(ctx):
    await ctx.message.delete()
    user2 = await ctx.guild.fetch_member(90286939487346688)
    response = random.choice([
            f"{ctx.author.mention} sybau 🥀💔 ",
            f"{ctx.author.mention} FUCK YOU",
            "ts so kevin 🥀",
            "gurt: yo","amongus","dabs seductively","🫃",":ericlove:",
            f"{user2.mention}",":head:","boots up hearthstone",
            "I’m on my Deriod cuh 😢💔",
            "I'm not loyal to anyone, i'm a demon",
            "You see this, I really did this, I'm him",
            "My money long, my pockets deep, no pocket watchin in these parts",
            "They must have amnesia because they forgot that I'm him."
        ])
    await ctx.send(response)

bot.run(token, log_handler=handler, log_level = logging.DEBUG)