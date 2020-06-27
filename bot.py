import os
import random
from discord.ext import commands
from dotenv import load_dotenv
import discord
from googletrans import Translator
import langdict

translator = Translator()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

cogs = ['cogs.Essentials', 'cogs.Moderation']
print("Startup Command Recieved")
prefix = input("Please Enter the Designated Command Prefix: " )
status= input("Please Enter the Designated Bot Status: ")
status = "Prefix: "+prefix+" | "+status

bot = commands.Bot(command_prefix=prefix,owner_id=379786876204220417,case_insensitive=True)
#bot.change_presence(activity=discord.Game("something")

for cog in cogs:
    bot.load_extension(cog)
    print("Loaded "+cog)
print("")

@bot.event
async def on_ready():
    #set status
    game = discord.Game(status)
    await bot.change_presence(status=discord.Status.online, activity=game)
    #list guilds bot are in and active
    for guild in bot.guilds:
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

print("Bot Started. Welcome Developer. ")

#welcome
@bot.event
async def on_member_join(member):
    await member.send('Hi {member.name}, welcome to the Discord server!')



#commands
@bot.command(name='members', help='list all members in the server')
async def members(ctx):
    ##await ctx.send("hi")
    ID = ctx.guild.id
    #print("SERVER ID: "+str(ID))
    for server in bot.guilds:
        if(ID == server.id):
            #print("FOUND SERVER")
            break
    members = '\n - '.join([member.name for member in server.members])
    await ctx.send(f'``` Members:\n - {members}```')

#roll and flip
@bot.command(name='rolldie', help ='rolls a die')
async def rolldie(ctx):
    await ctx.send("```Rolling Die: \n"+str(random.randint(1,6))+"```")
@bot.command(name='coinflip', help ='flips a coin')
async def coinflip(ctx):
    sides = ['heads', 'tails']
    await ctx.send("```Flipping Coin: \n"+str(random.choice(sides))+"```")


#translate command
@bot.command(name='translate', help = 'translates text to a desired language. Do '+prefix+'help translate for more info \n To use, first type the desired language and then type the sentence to translate in quotation marks (ex: "i am a person") \n For list of codes, go to \n https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages')
async def translate(ctx, desired, text):
    translated=(translator.translate(text, dest=desired)).text
    originlanguage = translator.detect(text).lang
    await ctx.send('` Translation from '+originlanguage+ ' to '+desired+
                                           '\n Translated Text:`'+translated)
#rock  paper scissors


'''
@bot.command(name='temp')
async def temp(ctx):
    await ctx.send("Someone post this on another discord")
    await ctx.send(file=discord.File('someone post this in another discord.jpg'))
'''
#hello and happ bday
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    helloquotes = ["Wassup Dude", "Hi. How are you?", "helllo from the other side",
                   "Gday Bro", "Hello", "hi"]

    if message.content == 'hello':
        response = random.choice(helloquotes)
        await message.channel.send(response)
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! Congrats! ')
    #else:
     #   text = message.content
     #   await message.channel.send((translator.translate(text)).text+" "+(translator.detect(text)).lang)
    #b/c discord.py prioritzies on_message over commands, we need to process commands too
    await bot.process_commands(message)



#autotranslate
@bot.listen()
async def on_message(message):
    if message.author ==bot.user:
        return
    text = message.content
    translatedraw = (translator.translate(text))
    langraw  = translator.detect(text)
    translatedfinal = translatedraw.text
    langfinal = langraw.lang
    #print(text[0])
    if(text[0]!= prefix):
        if(len(text)>5):
            if(langfinal.find("en")==-1):
                await message.channel.send('`Automatic Translation from '+langfinal+ ' to english'+
                                               '\n Translated Text:`'+translatedfinal)

'''
#automod
@bot.listen()
async def on_message(message):
    if message.author==bot.user:
        return
    text = message.content
    badwords = ['anal','anus','arse','ass','ballsack','balls','bastard','bitch','biatch','blowjob','blow job','bollock','bollok','boob','buttplug','clitoris','cock','coon','crap','cunt','dick','dildo','dyke','fag','feck','fellate','fellatio','felching','fuck','f u c k','fudgepacker','fudge packer','flange','homo','jerk','jizz','knobend','knob end','labia','muff','nigger','nigga','penis','piss','poop','prick','pube','pussy','queer','scrotum','sex','shit','s hit','sh1t','slut','smegma','spunk','tit','tosser'
'turd','twat','vagina','wank','whore','wtf', 'nibba', 's h i t']
    for x in badwords:
        if(x in text.lower()):
            await message.channel.send("No Cursing PLS")
            await message.delete()
            return

'''


#run bot with token
bot.run(TOKEN)
