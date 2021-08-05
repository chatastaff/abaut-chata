import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')  
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Tiktok/ex.121'))
    print('Bot Is Online')

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "yes", description = "To view commands type .help",color = ctx.author.color)  # embed title and description for .help command
    em.add_field(name = "Insta", value = ".insta")
    em.add_field(name = "Youtube", value = ".youtube")
    em.add_field(name = "TikTok", value = ".tiktok")
    em.add_field(name = "Twitter", value = ".twitter")
    em.add_field(name = "Github", value = ".github")
    em.add_field(name = "Website", value = ".website")
    em.set_image(url='https://cdn.discordapp.com/attachments/870559347992834122/872826617406304316/745-7453962_pepe-meme-rarepepe-gun-twitch-emotes-pepe-hd.png')
    em.set_thumbnail(url='https://cdn.discordapp.com/attachments/870559347992834122/872826544505122856/go.gif')
    await ctx.send(embed = em)
    
@client.group(invoke_without_command=True)
async def insta(ctx):
    em = discord.Embed(title = "ExT's Instagram", description = "https://www.instagram.com/extchasin/",color = ctx.author.color)
    await ctx.send(embed = em)

@client.group(invoke_without_command=True)
async def github(ctx):
    em = discord.Embed(title = "ExT's Github", description = "https://github.com/ExTTT",color = ctx.author.color)
    await ctx.send(embed = em)

@client.group(invoke_without_command=True)
async def website(ctx):
    em = discord.Embed(title = "ExT's Website", description = "https://ext121.ml/",color = ctx.author.color)
    await ctx.send(embed = em)    

@client.group(invoke_without_command=True)
async def youtube(ctx):
    em = discord.Embed(title = "ExT's Youtube", description = "https://www.youtube.com/channel/UChOtp5ZMM-NmubUGjKtgYIQ",color = ctx.author.color)
    await ctx.send(embed = em)    


@client.group(invoke_without_command=True)
async def tiktok(ctx):
    em = discord.Embed(title = "ExT's TikTok", description = "https://www.tiktok.com/@ex.121?lang=en",color = ctx.author.color)
    await ctx.send(embed = em)   


@client.group(invoke_without_command=True)
async def twitter(ctx):
    em = discord.Embed(title = "ExT's Twitter", description = "https://twitter.com/extsus",color = ctx.author.color)
    await ctx.send(embed = em)   

@client.event
async def message(msg):
    if 'skid' in msg.content:
        await client.send_message("https://tenor.com/view/spies-in-disguise-ratio-didnt-ask-dont-care-twitter-gif-22116633")

client.run('token goes here')
