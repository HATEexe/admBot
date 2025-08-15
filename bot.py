import os
import disnake
from dotenv import load_dotenv
from disnake.ext import commands

load_dotenv()

intents = disnake.Intents(
	bans = True,
	message_content = True,
	moderation = True,
	guild_messages = True,
	invites = True,
	members = True,
	voice_states = True,
	guilds = True,
)

bot = commands.Bot(command_prefix = disnake.ext.commands.when_mentioned, intents = intents)

@bot.event
async def on_ready():
	print("SYSTEM IS UP AND RUNNING")

bot.load_extensions('mods')

bot.run(os.getenv('TOKEN'))
