import discord
from discord.ext import commands
client = commands.Bot(command_prefix ="/")

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle , activity=discord.Game("helping people . "))
	print("ok")
@client.event
async def on_message(message):
	Nmessage = message.content
	if str(message.channel.type) == "private":
		Nmessage = message.content
		channel = client.get_channel(688788263321993277)
		embed=discord.Embed(title="Confession .",color=0x00ff00, description="A new confession  .")
		embed.add_field(name="Confession :", value=Nmessage, inline=False)
		await channel.send(embed=embed)
client.run("Njg3Mzk1NTU4NDc3NzkxMjQ1.Xm6OfQ.bTAPXPxKcUphYWGZpcfMRKwFyuc",bot=True)
