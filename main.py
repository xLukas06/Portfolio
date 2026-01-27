import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

ORIGIN_COLOR = 0x283AB8

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the Flow 🌊"))
    print(f'{bot.user} is stabilized and online.')

# --- COMMANDS ---

# 1. Clear messages (For Regulators/Sentinels)
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🌊 **Flow Restored:** {amount} messages cleared.", delete_after=5)

# 2. Studio Info
@bot.command()
async def studio(ctx):
    embed = discord.Embed(title="🌊 Flux Studios Interactive", color=ORIGIN_COLOR)
    embed.add_field(name="Current Status", value="🟢 Operational", inline=True)
    embed.add_field(name="Engine", value="Roblox / Flux-Core", inline=True)
    embed.set_footer(text="Maintaining the stream since 2026")
    await ctx.send(embed=embed)

bot.run('MTQ2NTcwNTY3MTI4OTk5NTI2NA.GgFx-S.-jrDIxg61fCDU_cOVZQWVuQirSg_NwQAHoA3dc')
