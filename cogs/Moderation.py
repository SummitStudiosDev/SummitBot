from discord.ext import commands
from datetime import datetime as d
from discord.ext.commands import has_permissions, CheckFailure


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot      
    @commands.command(
        name='mutechat',
        description='mutes the channel',
        help ="Mutes the channel"
    )
    @commands.has_permissions(manage_channels=True)
    async def mutechat(self, ctx):
        await ctx.send("``` Muting Chat ```")
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("``` Muted Chat! ```")
    #mutechat error
    @mutechat.error
    async def mutechat_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            text = f"Sorry {ctx.author}, you do not have permission to do that!"
            await ctx.send (text) 

    
    @commands.command(
        name='unmutechat',
        description='unmutes the channel',
        help ="Unmutes the channel"
    )
    @commands.has_permissions(manage_channels=True)
    async def unmutechat(self, ctx):
        await ctx.send("``` Unmuting Chat ```")
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send("``` Unmted Chat! ```")
    @unmutechat.error
    async def unmutechat_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            text = f"Sorry {ctx.author}, you do not have permission to do that!"
            await ctx.send (text) 
        



    


def setup(bot):
    bot.add_cog(Moderation(bot))
