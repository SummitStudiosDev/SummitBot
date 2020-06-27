from discord.ext import commands
from datetime import datetime as d

class Essentials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot      
    @commands.command(
        name='ping',
        description='The ping command',
        aliases=['p'],
        help ="Pings the Bot"
    )
    async def ping_command(self, ctx):
            start = d.timestamp(d.now())
            msg = await ctx.send(content='Pinging')
            await msg.edit(content=f'Pong!\nOne message round-trip took {( d.timestamp( d.now() ) - start ) * 1000 }ms.')
            return
    #about command
    @commands.command(name='about', help = 'about the bot')
    async def about(self, ctx):
        await ctx.send("```SummitBOT was created by user Destined_ToDefeat#2348 and was programmed in Python```")
        await ctx.send("```Translation Services Are Powered by Google Translate API```")
    #calc command
    @commands.command(name='calc', help = 'syntax: calc num1 operation num2 (valid operations: * / + - %) ')
    async def calc(self, ctx, num1, operation, num2):
        if(operation == "+"):
            num1=int(num1)
            num2=int(num2)
            answer = num1+num2
            await ctx.send('``` Calculated: '+str(num1)+"+"+str(num2)+"\n Result: "+str(answer)+"```")
        elif operation =="-":
            answer = int(num1)-int(num2)
            await ctx.send('``` Calculated: '+str(num1)+"-"+str(num2)+"\n Result: "+str(answer)+"```")
        elif operation == "*":
            num1=int(num1)
            num2=int(num2)
            answer = num1*num2
            await ctx.send('``` Calculated: '+str(num1)+"*"+str(num2)+"\n Result: "+str(answer)+"```")
        elif operation == "/":
            num1=int(num1)
            num2=int(num2)
            answer = num1/num2
            await ctx.send('``` Calculated: '+str(num1)+"/"+str(num2)+"\n Result: "+str(answer)+"```")
        elif operation == "%":
            num1=int(num1)
            num2=int(num2)
            answer = num1%num2
            await ctx.send('``` Calculated: '+str(num1)+"%"+str(num2)+"\n Result: "+str(answer)+"```")
        else:
                await ctx.send("```Please enter a valid operation```")



    


def setup(bot):
    bot.add_cog(Essentials(bot))
