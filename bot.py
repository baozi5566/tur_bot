import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix= '[', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1208697980467814470)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1208698019763982387)
    await channel.send(f'{member} leave!')

bot.run("MTIwODY3MzEwNTM4NDU3NDk4Ng.GR1Dzg.6dpH2VBwV7y8h7AwmM-rOsL8WqeMOUVimF4t7Q")