import datetime
import logging
import discord 
from discord.ext import commands
import json
epoch = datetime.datetime.utcfromtimestamp(0)
TOKEN='NjkwMjcyNjA4MzA2MDY5NjE2.XnTRQg.1bEwIx53VzOsQXzp3jj5Ya0U9D8'
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
	print("online")




@client.event
async def on_member_join(member):
    with open('money.json', 'r') as f:
        users = json.load(f)


    await update_data(users, member)

    
    with open('money.json', 'w') as f:
        json.dump(users, f)



@client.event
async def on_message(message):
	if message.author.bot == False:
		with open('money.json', 'r') as f:
			users = json.load(f)
		await update_data(users, message.author)
		await add_experience(users, message.author, 5)
		await level_up(users, message.author, message)
		with open('money.json', 'w') as f:
			json.dump(users, f)
		await client.process_commands(message)
	
async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1
        
        users[f'{user.id}']['xp_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
		
async def add_experience(users, user, exp):
	
	time_diff = ((datetime.datetime.utcnow() - epoch).total_seconds() - users[f'{user.id}']['xp_time'])
	if time_diff >= 30: 
   	 users[f'{user.id}']['experience'] += exp
   	 users[f'{user.id}']['xp_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
	

async def level_up(users, user, message):
    experience = int(users[f'{user.id}']['experience'])
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1/4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end
        
        
    if (300<=experience<=600):
    	role = discord.utils.get(user.guild.roles , name="Kogal")
    	await user.add_roles(role)
    if (601<=experience <=3000):
    	role = discord.utils.get(user.guild.roles , name="Office Lady")
    	await user.add_roles(role)
    if(3001<=experience<=600):
    	role = discord.utils.get(user.guild.roles , name="Tsundere")
    	await user.add_roles(role)
    if (6001<=experience <=11000):
    	role = discord.utils.get(user.guild.roles , name="Pettanko")
    	await user.add_roles(role)
    if (11001<=experience <=15860):
    	role = discord.utils.get(user.guild.roles , name="Succubus")
    	await user.add_roles(role)
    if (15861<=experience <=35000):
    	role = discord.utils.get(user.guild.roles , name="Tentacle Beast")
    	await user.add_roles(role)
    if (35001<=experience <=80000):
    	role = discord.utils.get(user.guild.roles , name="Yandere")
    	await user.add_roles(role)
    if (80001<=experience<=100000):
    	role = discord.utils.get(user.guild.roles , name="Futanari")
    	await user.add_roles(role)
    if (experience>100000):
    	role = discord.utils.get(user.guild.roles , name="Onee-sama")
    	await user.add_roles(role)  
    
    	
    	
    	
@client.command()
async def rank(ctx):
	with open('money.json', 'r') as f:
			users = json.load(f)
	member=ctx.author
	user_id=str(member.id)
	embed=discord.Embed(title=f"Rank of {member}", color=0x00ffff)
	embed.add_field(name="Level", value=users[f'{user_id}']['level'], inline=False)
	embed.add_field(name="Xp", value=
	users[f'{user_id}']['experience'], inline=True) 
	await ctx.send(embed=embed)


			
	
	
client.run(os.getenv('TOKEN'))
