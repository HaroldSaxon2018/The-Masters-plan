import discord 
from discord.ext	import commands
import asyncio 
import time


client = commands.Bot(command_prefix =('.')) 

@client.listen()
async def on_ready(): 
	print('Logged in as') 
	print(client.user.name)
	print(client.user.id) 
	print('------') 

@client.command()
async def ping(ctx):
    await ctx.send(f'🏓 Pong! `{ctx.bot.latency * 1_000:,.0f}ms` ')
    
@client.command()
async def hello(ctx):
	await ctx.send('Ello, How may i be of service to you.....')
	
@client.command()
async def goodbye(ctx):
	await ctx.send('Fine, I see how it is, Just Leave!!!')

@client.command(pass_context= True)
async def info(ctx):
    channel= ctx.channel
    embed= discord.Embed(
        title = 'Information',
        description = 'These are the commands',
        colour = 0xff0000   
)

    embed.set_footer(text= 'this is my footer.')

    embed.set_thumbnail(url= 'https://gyazo.com/e3408171d788fb5eb591e665e989fe66')

    embed.set_author(name= 'HaroldSaxon', icon_url= 'https://gyazo.com/e3408171d788fb5eb591e665e989fe66')

    embed.add_field(name= '.ping', value= 'to get the bots latency', inline=False)
    
    embed.add_field(name= '.hello', value= 'says hello', inline=False)

    embed.add_field(name= '.goodbye', value= 'says goodbye', inline=False)

    embed.add_field(name= '.info', value= 'provides this message', inline=False)

    await ctx.send(embed=embed)
 
 

client.run('TOKEN')
