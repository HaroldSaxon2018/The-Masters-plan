import discord 
from discord.ext	import commands
import asyncio 
import time
from discord.utils import get

client = commands.Bot(command_prefix=commands.when_mentioned_or('.','<@547604715412652033>')) 

@client.listen()
async def on_ready(): 
 print('Termux is logged in as') 
 print(client.user.name)
 print(client.user.id) 
 print('------') 
 await client.change_presence(activity=discord.Game(name='''around with adding roles'''))

@client.command()
async def ping(ctx):
 await ctx.send(f'🏓 Pong! `{ctx.bot.latency * 1_000:,.0f}ms`')
    
@client.command()
async def hello(ctx):
 await ctx.send(f"Ello {ctx.author.mention},                                                       How may i be of service to you.....")
	
@client.command()
async def goodbye(ctx):
 await ctx.send(f"Fine {ctx.author.mention},                                                           just leave, get outta here.....")

client.remove_command('help')

@client.command()
async def help(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = 'Server Commands                                                    U.N.I.T. Prefixes {  .  } or {  @bot.mention  }',
 description = 'This is the current list of commands',
 colour = 0xff0000   
 )

 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= '.help', value= 'Provides this message.', inline=False)
 
 embed.add_field(name= '.unit_help', value= '''Provides commands especially for our Faction''', inline=False)
 
 embed.add_field(name= '.drpg_help', value= 'Provides the help message for Discord Dungeons.', inline=False)

 embed.add_field(name= '.ping', value= 'Returns the bots latency. ', inline=False)
 
 embed.add_field(name= '.hello', value= 'Says Hello!', inline=False)

 embed.add_field(name= '.goodbye', value= 'Says Goodbye', inline=False)
 
 await ctx.send(embed=embed)

@client.command()
async def drpg_help(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = "Discord Dungeons help commands",
 description = 'The Prefix for Discord Dungeons is [   #!   ]',
 colour = 0xff0000   
 )
 
 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= '.starting_drpg', value= 'Provides a guide to Discord Dungeons', inline=False)
 
 embed.add_field(name= '.drpg_attributes', value= 'Shows a guide of the different attributes', inline=False)
 
 embed.add_field(name= '.drpg_sides', value= 'Shows a guide of the different sides and thier commands', inline=False)
 
 embed.add_field(name= '.drpg_timers', value= 'Shows a guide of the different timer commands', inline=False)
 
 embed.add_field(name= '.drpg_market', value= 'Shows a guide of the different market commands', inline=False)
 
 embed.add_field(name= '.drpg_globalmarket', value= 'Shows a guide of the different global market commands', inline=False)
 
 embed.add_field(name= '.drpg_tools', value= 'Shows a guide of the different tools', inline=False)
 
 embed.add_field(name= '.drpg_quests', value= 'Shows a guide of the different Quests', inline=False)

 await ctx.send(embed=embed)
 
@client.command()
async def unit_help(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = 'Faction Commands',
 description = 'This is a list of faction commands',
 colour = 0xff0000   
 )

 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= '.server_rules', value= 'Provides the rules of the server', inline=False)
 
 embed.add_field(name= '.faction_rules', value= 'Provides the rules of the Faction', inline=False)
 
 embed.add_field(name= '.next_goal', value= 'Provides the next goal for the Faction', inline=False)
 
 embed.add_field(name= '.e_count', value= 'Provides rules for a Energy count', inline=False)
 
 await ctx.send(embed=embed)
 
@client.command()
async def server_rules(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = "Server Rules",
 description = 'These are the rules of the server',
 colour = 0xff0000   
 )

 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= '01.', value= 'No spamming.', inline=False)

 embed.add_field(name= '02', value= 'No advertising. ', inline=False)
 
 embed.add_field(name= '03.', value= 'Keep chat in designated channels. No NSFW!', inline=False)
 
 embed.add_field(name= '04.', value= 'Keep games in thier appropriate channels.', inline=False)
 
 embed.add_field(name= '05.', value= 'This is primarily an english server. As such, please keep any non-english communication to #basement.', inline=False)
 
 embed.add_field(name= '06.', value= 'Keep your shitposting in #basement. ', inline=False)
 
 embed.add_field(name= '07.', value= '''If a ``Captain`` tells you to stop doing something, listen to them. It doesn't matter if it's specifically stated here.''', inline=False)
 
 embed.add_field(name= '08.', value= 'Use common sense. ', inline=False)

 embed.add_field(name= '09.', value= '''If you would like to begin playing DiscordRPG, type ``b! startingdrpg`` 
If you need help, please feel free to ping me or send a DM.''', inline=False)

 await ctx.send(embed=embed)

@client.command()
async def faction_rules(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = "Faction Rules",
 description = 'These are the rules of the Faction',
 colour = 0xff0000   
 )

 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= '01.', value= '''__***Under No Circumstances***__ attack another member of the Faction. 
Unless it's for Mug Protection or to remove Bounties.''', inline=False)

 embed.add_field(name= '02.', value= '''__***NO SCAMMING***__ 
Do not scam other members,  if provided with evidence, you will be dismissed.''', inline=False)
 
 embed.add_field(name= '03.', value= '''__***NO BEGGING***__ of any kind. 
Meds and drugs will be provided for chains and territory wars only.''', inline=False)
 
 embed.add_field(name= '04.', value= '''From the ***1st*** - ***14th*** we **Train**,
From the ***15th*** - ***29th*** we **Chain**, 
The rest of the month is yours to spend **Energy** as you please.''', inline=False)

 await ctx.send(embed=embed)

@client.command()
async def e_count(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = 'E-count',
 description = 'How to do an E-count',
 colour = 0xff0000   
 )

 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= 'When doing an E count, Please convert your Energy in to hits', value= '''

__**Non-Donator Status**__
Natural E = 100 E= 4 hits 
Xan + NE = 350 E= 14 hits
2x Xan + NE = 600 E = 24 hits
3x Xan + NE = 850 E = 34 hits
A Points Refill is an additional 4 hits
FHC is also an additional 4 hits 

__**Donator Status**__
Natural E = 150 E= 6 hits 
Xan + NE = 400 E = 16 hits
2x Xan + NE = 650 E = 26 hits
3x Xan + NE = 900 E = 36 hits
A Points Refill is an additional 6 hits
FHC is also an additional 6 hits  


That way it is easier for our Chain Captains to get an accurate count for the planned chain.

''', inline=False)

 await ctx.send(embed=embed)

@client.command()
async def starting_drpg(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = "Guide to Discord Dungeons",
 description = 'The Prefix for Discord Dungeons is [   #!   ]',
 colour = 0xff0000   
 )

 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= 'Getting Started', value= '''Prior to starting your adventure, you will need to do #!stats to create your Discord Dungeons character.

For each level you have reached, you will be granted 5 unassigned skill points also an additional 50 health along with full health. It is recommended to assign all of your unassigned skill points. You can assign skill points by entering #!assign <stat> <amount>.

Example : #!assign xpboost all

See : ``.drpg_attributes``''', inline=False)

 await ctx.send(embed=embed)

@client.command()
async def drpg_attributes(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = "Guide to Discord Dungeons",
 description = 'The Prefix for Discord Dungeons is [   #!   ]',
 colour = 0xff0000   
 )

 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= 'Attributes', value= '''These are the attributes you can assign your points too

+ Criticals: 0 (+0%)         • Formula : x/40 = 1%
+ Defense: 0 (-0 dmg)    • Formula : x/10 = 1
+ Gold Boost: 0 (+0%)   • Formula : x/10 = 1%
+ Lumber Boost: 0 (+0)  • Formula : x/25 = 1
+ Mine Boost: 0              • Formula : x/40 = 1
+ Reaping: 0                  • Formula : More = Better 
+ Salvaging: 0                • Formula : More = Better
+ Scavenging: 0             • Formula : x/65 = 1
+ Strength: 0 (+0 dmg)   • Formula : x/10 = 1
+ Taming: 0                     • Formula : More = Better
+ XP Boost: 0 (+0)          • Formula : x/10 = 1

Unsure which stat build to do or not sure which stats to assign points with?
Here is the most recommended stat build to follow at the moment:

A build focused on XP Boost

A build focused on XP Boost and Gold Boost.''', inline=False)

 await ctx.send(embed=embed)
 
@client.command()
async def drpg_sides(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = "Guide to Discord Dungeons",
 description = 'The Prefix for Discord Dungeons is [   #!   ]',
 colour = 0xff0000   
 )
 
 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= 'Sides', value= '''To begin u can only use #!forage and #!search

You must purchase a pickaxe for #!mine and an axe for #!chop and a fishing rod for #!fish at lvl 5

Your Sides :: #!chop, #!mine, #!forage, #!fish all have a 300 second timer (5 minutes)
And #!search has a 600 second timer  (10 minutes)''', inline=False)

 await ctx.send(embed=embed)
 
@client.command()
async def drpg_timers(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = "Guide to Discord Dungeons",
 description = 'The Prefix for Discord Dungeons is [   #!   ]',
 colour = 0xff0000   
 )
 
 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= 'Timers', value= '''Use ``&uconfig adventureTimer on`` for an #!adv timer


Use ``&uconfig sidesTimer on`` for a Sides timer


Use ``&uconfig traverTimer on`` for a travel timer (you can only travel once you obtain a compass)


Use ``&uconfig healthMonitor 30`` for a Heath alert when your health falls below 30%''', inline=False)

 await ctx.send(embed=embed)
 
@client.command()
async def drpg_market(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = "Guide to Discord Dungeons",
 description = 'The Prefix for Discord Dungeons is [   #!   ]',
 colour = 0xff0000   
 )
 
 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= 'Market', value= '''You can check a list of items by using 
``#!items [page]`` 

Then retrieve the details of an item with 
``#!item [item]``.
''', inline=False)

 await ctx.send(embed=embed)
 
@client.command()
async def drpg_globalmarket(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = "Guide to Discord Dungeons",
 description = 'The Prefix for Discord Dungeons is [   #!   ]',
 colour = 0xff0000   
 )
 
 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= 'Global Market', value= '''The global market allows player to sell or buy items from other players.

``#!gmglist [page]`` 
Lists all selling trades.

``#!gmsell [item] [amount to sell] [price per item]`` 
Puts a selling trade up on the global market.

``#!gmsearch [item] [page]`` 
Searches for selling trades of said item on the global market.

``#!gmbuy [trade id] [amount to buy]`` 
Executes a selling trade on the global market for the specified quantity of items.

``#!gblist [page]`` 
Lists all buying trades.

``#!gbbuy [item] [amount to buy] [price per item]`` 
Puts a buying trade up on the global market.

``#!gbsearch [item] [page]`` 
Searches for buying trades of said item on the global market.

``#!gbsell [trade id] [amount to buy]`` 
Executes a buying trade on the global market for the specified quantity of items.

``#!gmstop [trade id]`` 
Ends a trade, returning gold and unsold items or items and unspent gold to your inventory.

``#!gmlist [pagenumber]`` 
Lists your trades.

Note: A maximum of 5 trades (10 for users with drpg membership) can be put up at the same time.
.''', inline=False)

 await ctx.send(embed=embed)

@client.command()
async def drpg_tools(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = "Guide to Discord Dungeons",
 description = 'The Prefix for Discord Dungeons is [   #!   ]',
 colour = 0xff0000   
 )
 
 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= 'Tools', value= '''Tools are used to get more items from side activities

Tools for mining and chopping are regularly spaced and craftable. The first set of tools (Axe, Pickaxe) must be bought from the normal store using the #!buy command. The rest of the tools for these two side activities must be crafted. 

At skill level 2, the Copper tools may be used. 
At skill level 5, the zinc tools may be used . 
At skill level 10, Iron tools are available, 
At skill level 15, steel tools are available, 
and finally leptocite tools become available at skill level 30.

The True Wood Cutter is available at level 12 after completing A Quest About Wood?, and is equivalent to the Zinc Axe.

The fishing side activity is available at level 5, at which point the Fishing Rod may be bought from the store. The only upgrade to the fishing rod is the Angler's Rod, which is available at level 25, after completing Fickle Fishing.
''', inline=False)

 await ctx.send(embed=embed)
 
@client.command()
async def drpg_quests(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = "Guide to Discord Dungeons",
 description = 'The Prefix for Discord Dungeons is [   #!   ]',
 colour = 0xff0000   
 )
 
 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')
 
 embed.add_field(name= '[Non-member Quests]', value= '''Cult of MOUKN
The Cold North
Fickle fishing
The quest about wood?
Meditative Magic
Exotic Eggnog
The Land Above
Namazu
How to keep a mummy''', inline=False)

 embed.add_field(name= '[Member Quests]', value= '''Baffling Baking
Dragon Slayer 
Menu Specials
Bakoushi's Bunny
Mystic Gravestone''', inline=False)
 
 embed.add_field(name= '[Expired Quest]', value= '''Spooktober Spectacle (4th November 2017)
Trick or Treat (4th November 2017)''', inline=False)

 await ctx.send(embed=embed)
 
@client.command()
async def next_goal(ctx):
 channel= ctx.channel
 embed= discord.Embed(
 title = "Our Next Goal",
 description = 'What will our next upgrade be???',
 colour = 0xff0000   
 )
 
 embed.set_footer(text= 'Brought to you by HaroldSaxon. VOTE SAXON!!!!')

 embed.set_author(name= 'U.N.I.T.', icon_url= 'https://i.gyazo.com/0efdd732da7cdd7109204586b99450e7.png')

 embed.add_field(name= 'Travel capacity II', value= '''
 Increases maximum item capacity while travelling by 2

Requires: 1,349 respect''', inline=False)

 await ctx.send(embed=embed)

@client.event
async def on_member_join(member):
 role = discord.utils.get(ctx.guild.roles, name="Members") 
 user = ctx.message.author 
 await user.add_roles(role)
 
# from here down is what I am trying to test
	
@client.command(pass_context=True)
async def yt(ctx): 
 url = ctx.message.content 
 url = url.strip('yt ') 
 author = ctx.message.author 
 voice_channel = author.voice_channel 
 vc = await client.join_voice_channel(voice_channel) 
 player = await vc.create_ytdl_player(url) 
 player.start()
 
@client.command(pass_context=True)
async def tidy(ctx, amount=100):
 channel= channel.purge(limit=limit)
 message= []
 async for message in client.logs_from(channel, limit= int(amount)+ 1):
  message.append(message)
 await client.delete_messages(messages)
 await client.say('messages are deleted')
 
 
@client.command(pass_context=True)
@commands.has_role("test role")
async def addrole(ctx): 
 member = ctx.message.author 
 role = get(member.server.roles, name="test role") 
 await bot.add_roles(member, role)
 
 
client.run('NTQ3NjA0NzE1NDEyNjUyMDMz.D2CMmw.PkWciaqxg82VmTMyu_fc98rHCxg')
