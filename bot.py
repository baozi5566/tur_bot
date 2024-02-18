import discord
from discord.ext import commands
import json 
import random
import os
import asyncio
with open('setting.json', 'r', encoding="utf8") as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix= '[', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member} leave!')

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-loaded {extension} done.')

async def load_extensions():
    for filename in os.listdir("./cmds"):
        if filename.endswith(".py"):
            #cut off the .py from the file name
            await bot.load_extension(f"cmds.{filename[:-3]}")
    
async def main():
    async with bot:
        await load_extensions()
        await bot.start(jdata['TOKEN'])

if __name__=="__main__":
    asyncio.run(main())
