import discord
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix = '>')

SECRET_KEY = os.getenv("TOKEN")

@client.event
async def on_ready():
    print('Bot is ready!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


        
client.run(SECRET_KEY)