import hashlib
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from datetime import datetime

client = Bot(command_prefix=".")

@client.event
async def on_ready():
  print("Bot activated at " + datetime.now().strftime("%D %H:%M:%S"))

@client.command()
async def kill(ctx):
  if hashlib.sha3_512(ctx.message.author.id.encode("utf-8").hexdigest()) == "9f5ff27bae96e312e021d2e84b3ea04b47c59cd3e610b2d0be06fd141b61eb25b5e1c1c9343b4fe93a63fde20117de4f534218ac05f24bc0d7f7d0c30020f484":
    ctx.bot.logout()
  else:
    await ctx.message.send(f"<@{ctx.message.author.id}> Unauthorized command.")

client.run(open("token.txt",'r').read())