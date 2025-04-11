import discord
from discord.ext import commands
import yaml

# Load bot_token from a YAML file
with open("discord_bot_key.yaml", "r") as file:
    config = yaml.safe_load(file)
    bot_token = config.get("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - {bot.user.id}")
    print("------")

@bot.command()
async def list_threads(ctx):
    channel = ctx.channel

    # Get active and archived public threads
    threads = await channel.threads()  # requires discord.py >=2.0

    if not threads:
        await ctx.send("No threads found in this channel.")
        return

    thread_names = [f"- {thread.name}" for thread in threads]
    response = "**Threads in this channel:**\n" + "\n".join(thread_names)
    await ctx.send(response)

bot.run(bot_token)
# This bot lists all threads in the channel where the command is invoked.