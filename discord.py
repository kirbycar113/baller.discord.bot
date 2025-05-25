import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

@bot.command()
async def saybot(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def announce(ctx, *, message):
    if discord.utils.get(ctx.author.roles, name='Admin'):
        await ctx.send(message)
    else:
        await ctx.author.send("❌ You don't have permission to use the /announce command.")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def emergency(ctx):
    await ctx.send('🚨 **CODE RED** 🚨')
    owner = ctx.guild.owner
    if owner:
        try:
            await owner.send(f'🚨 Code Red triggered by {ctx.author.mention} in **{ctx.guild.name}**!')
        except discord.Forbidden:
            await ctx.send("Couldn't DM the server owner.")
    else:
        await ctx.send("No server owner found.")

token = os.getenv('TOKEN')
if not token:
    print("Error: TOKEN environment variable not found!")
else:
    bot.run(token)
