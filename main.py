import hashlib
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from datetime import datetime

client = Bot(command_prefix=".")
authHashes = ["9f5ff27bae96e312e021d2e84b3ea04b47c59cd3e610b2d0be06fd141b61eb25b5e1c1c9343b4fe93a63fde20117de4f534218ac05f24bc0d7f7d0c30020f484","26c92d0a7e01bf43a3c1f3e6de0407e9b4ec4762c530a13fafefe51d33257519c8cb839b149e3565ee92c63de9fee2e3b295efc75f89dd99cb5f97d5cb668d46"]

@client.event
async def on_ready():
  print("Bot activated at " + datetime.now().strftime("%D %H:%M:%S"))

@client.command()
async def exit(ctx):
  if hashlib.sha3_512(str(ctx.message.author.id).encode("utf-8")).hexdigest() in authHashes:
    await ctx.send("Shutting down...")
    await ctx.bot.logout()
  else:
    await ctx.send(f"<@{ctx.message.author.id}> Unauthorized command.")

client.run(open("token.txt",'r').read())