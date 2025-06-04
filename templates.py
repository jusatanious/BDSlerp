import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

import random
import asyncio

# ctrl c to stop the bot


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)#, help_command=None)

@bot.event
async def on_ready():
    print(f"Bot is ready!, {bot.user.name}")
    

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome {member.name} to the server!")

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


    if "Devin" in message.content.lower():
        await message.delete()
        #                                 @ mentions user
        await message.channel.send(f"{message.author.mention} - Who?")
    # Process commands if any
    await bot.process_commands(message)
    
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")

@bot.command()
@commands.has_role("Admin")  # Only users with the Admin role can use this command
async def admin(ctx):
    await ctx.send("You are a big boss!")
@admin.error
async def admin_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You do not have the required role to use this command.")
    else:
        await ctx.send("An error occurred while processing your command.")

#DM
@bot.command()
async def dm(ctx,*,msg):
    await ctx.author.send(f"Yoooooooo {msg}")
#Bot respond
@bot.command()
async def reply(ctx):
    await ctx.reply("This is a reply to your message!")

@bot.command()
async def poll(ctx,*,question):
    embed = discord.Embed(title="Big Poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")


        
"""                   
assign or disassign a role to the user
@bot.command()
async def assign(ctx):
    #                                         role name
    role = discord.utils.get(ctx.guild.roles, name=u_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} has been assigned the role {u_role}!")
    else:
        await ctx.send("Does not exist")
@bot.command()
async def remove(ctx):
    #                                         role name
    role = discord.utils.get(ctx.guild.roles, name=u_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} has been assigned the role {u_role}!")
    else:
        await ctx.send("Does not exist")
"""

bot.run(token, log_handler=handler, log_level = logging.DEBUG)