import subprocess
import discord
frim discord.ext import commands
import asyncio

client = discord.Client(command_prefix=".", activity=discord.CustomActivity("This is basically SSH"))

TOKEN = "

@client.event
async def on_ready():
	print("Ready!")
	
@client.command(pass_context=True)
async def run(ctx):
	await ctx.send(ctx.message[4:])
	
client.run(TOKEN)
