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


@client.command()
async def info(ctx):
	await ctx.send('Ello, need some help huh,\n\n .ping\n .hello\n .goodbye\n .info\n\nThese are the available commands at this time.....')
	

client.run('TOKEN')
