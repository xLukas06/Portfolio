import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.messages = True 

bot = commands.Bot(command_prefix='!', intents=intents)

ORIGIN_COLOR = 0x283AB8
LOG_CHANNEL_ID = 1465707503752053002

@bot.event
async def on_ready():
    print(f'Flux Utility is stabilized.')

@bot.event
async def on_message_delete(message):
    if message.author.bot: return
    
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    embed = discord.Embed(title="🗑️ Message Deleted", color=0xFF0000)
    embed.add_field(name="Author", value=message.author.mention, inline=True)
    embed.add_field(name="Channel", value=message.channel.mention, inline=True)
    embed.add_field(name="Content", value=message.content or "No text (likely an image)", inline=False)
    await log_channel.send(embed=embed)

@bot.event
async def on_message_edit(before, after):
    if before.author.bot: return
    if before.content == after.content: return

    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    embed = discord.Embed(title="✏️ Message Edited", color=0xFFA500)
    embed.add_field(name="Author", value=before.author.mention, inline=True)
    embed.add_field(name="Channel", value=before.channel.mention, inline=True)
    embed.add_field(name="Before", value=before.content, inline=False)
    embed.add_field(name="After", value=after.content, inline=False)
    await log_channel.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🌊 **Flow Restored:** {amount} messages cleared.", delete_after=5)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("⚠️ **Protocol Breach:** You do not have permission to clear the flow.", delete_after=5)

bot.run('MTQ2NTcwNTY3MTI4OTk5NTI2NA.GgFx-S.-jrDIxg61fCDU_cOVZQWVuQirSg_NwQAHoA3dc')
