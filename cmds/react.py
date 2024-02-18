import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding="utf8") as jfile:
    jdata = json.load(jfile)

class react(Cog_Extension):
    @commands.command()
    async def 圖片(self, ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)

    @commands.command()
    async def web圖片(self, ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

async def setup(bot):
   await bot.add_cog(react(bot))
