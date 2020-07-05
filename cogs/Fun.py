from discord.ext import commands
import random

class Fun(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    #roll and flip
    @commands.command(name='rolldie', help ='rolls a die')
    async def rolldie(self, ctx):
        await ctx.send("```Rolling Die: \n"+str(random.randint(1,6))+"```")
    @commands.command(name='coinflip', help ='flips a coin')
    async def coinflip(self, ctx):
        sides = ['heads', 'tails']
        await ctx.send("```Flipping Coin: \n"+str(random.choice(sides))+"```")

    @commands.command(name='rockpaperscissors', help='rock paper scissors!', aliases=['rps'])
    async def rockpaperscissors(self, ctx):
        await ctx.send("```Started game of Rock Paper Scissors. Please type your choice```")
        await ctx.send("``` Type rock, paper, or scissors ```")
        message = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        msg = message
        msg = msg.content
        msg = str(msg)
        msg = msg.lower()
        #msg = msg.content()
        #await ctx.send(msg)
        if(msg != "rock" and msg != "paper" and msg != "scissors" and msg != "scissor"):
            await ctx.send("```It appears you have not chosen a valid choice. Please start a new game```")
            return

        if(msg == "scissor"):
            msg="scissors"
        urchoice = msg
        cchoice=random.randint(1,3)
        if cchoice==1:
            cchoice="rock"
              
        elif cchoice==2:
            cchoice="scissors"
               
        elif cchoice ==3:
            cchoice="paper"


        if(cchoice=="paper" and urchoice=="rock"):
            await ctx.send(" The computer has won")
            await ctx.send("The computer chose "+cchoice+ ". You chose "+urchoice)
            
        elif(cchoice=="scissors" and urchoice=="paper"):
            await ctx.send(" The computer has won")
            await ctx.send("The computer chose "+cchoice+ ". You chose "+urchoice)
            
        elif(cchoice=="rock" and urchoice=="scissors"):
            await ctx.send(" The computer has won")
            await ctx.send("The computer chose "+cchoice+ ". You chose "+urchoice)
                
        elif(cchoice=="scissors" and urchoice=="rock"):
            await ctx.send(" You have won!")
            await ctx.send("The computer chose "+cchoice+ ". You chose "+urchoice)
               
        elif(cchoice=="rock" and urchoice=="paper"):
            await ctx.send(" You have won!")
            await ctx.send("The computer chose "+cchoice+ ". You chose "+urchoice)
                
        elif(cchoice=="paper" and urchoice=="scissors"):
            await ctx.send(" You have won!")
            await ctx.send("The computer chose "+cchoice+ ". You chose "+urchoice)
                
        elif(cchoice=="paper" and urchoice=="paper"):
            await ctx.send(" Tie. ")
            await ctx.send("The computer chose "+cchoice+ ". You chose "+urchoice)
              
        elif(cchoice=="scissors" and urchoice=="scissors"):
            await ctx.send(" Tie. ")
            await ctx.send("The computer chose "+cchoice+ ". You chose "+urchoice)
                
        elif(cchoice=="rock" and urchoice=="rock"):
            await ctx.send(" Tie. ")
            await ctx.send("The computer chose "+cchoice+ ". You chose "+urchoice)



def setup(bot):
    bot.add_cog(Fun(bot))
