import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class basicComs(Cog_Extension):   
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}(ms)")
            
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="About", url="https://zh.wikipedia.org/zh-tw/%E8%B1%AC%E5%93%A5%E4%BA%AE", description="About the bot", color=0xf50000,
                            timestamp=datetime.datetime.now())
        embed.set_author(name="豬大哥", url="https://www.instagram.com/ckl.culture/", icon_url="https://www.chinapress.com.my/wp-content/uploads/2017/05/zhu-170515-b1-noresize.jpg")
        embed.set_thumbnail(url="https://scontent.frmq2-2.fna.fbcdn.net/v/t39.30808-6/360090358_288450130392752_6617976287399344178_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=783fdb&_nc_ohc=WActDAFOJP4AX_DJjvu&_nc_ht=scontent.frmq2-2.fna&oh=00_AfAquUqKfgLQcZRlPV3f1CJWZjJxPYTqvqTtrwW1LuittQ&oe=65D7B41C")
        embed.add_field(name="1", value="undefined", inline=True)
        embed.add_field(name="2", value="undefined", inline=True)
        embed.add_field(name="3", value="undefined", inline=False)
        embed.add_field(name="4", value="undefined", inline=False)
        embed.set_footer(text="1651651")
        await ctx.send(embed=embed)


    @commands.command()
    async def copy(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num : int):
        await ctx.channel.purge(limit=num+1)

   
    

async def setup(bot):
    await bot.add_cog(basicComs(bot))