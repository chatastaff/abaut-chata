import discord
from discord.ext import commands



client = commands.Bot(command_prefix = '.')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Tiktok/ex.121'))
    print('Bot Is Online')



@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Dumbass", description = "To view commands type .help",color = ctx.author.color)
    em.add_field(name = "Insta", value = ".insta")
    em.add_field(name = "Youtube", value = ".youtube")
    em.add_field(name = "TikTok", value = ".tiktok")
    em.add_field(name = "Twitter", value = ".twitter")
    em.set_image(url='https://cdn.discordapp.com/attachments/829487886352777266/837879211204411432/giphy.gif')
    em.set_thumbnail(url='https://cdn.discordapp.com/attachments/830639842483634258/837879663577137172/image0.png')
    await ctx.send(embed = em)
    
@client.group(invoke_without_command=True)
async def insta(ctx):
    em = discord.Embed(title = "ExT's Instagram", description = "https://www.instagram.com/ext.121/",color = ctx.author.color)
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
    em = discord.Embed(title = "ExT's Twitter", description = "https://twitter.com/OnlyCashing",color = ctx.author.color)
    await ctx.send(embed = em)   






client.run('TOKEN')
