import locale
import discord
from discord import utils
from discord.ext import commands
import time


# noinspection PyShadowingNames
def __init__(self, bot: commands.Bot):
    self.bot = bot


locale.setlocale(locale.LC_ALL, "en_US.utf8")
start_time = time.time()
bot = commands.Bot(command_prefix="!",
                   case_insensitive=True,
                   owner_id="")


@bot.event
async def on_ready():
    """Output after the Bot fully loaded"""
    end_time = time.time() - start_time
    await bot.change_presence(status=discord.Status.online)
    print(f'#-------------------------------#\n'
          f'| Username: {bot.user.name}\n'
          f'| User ID: {bot.user.id}\n'
          f'| Developer: CodingSquad Team\n'
          f'| Guilds: {len(bot.guilds)}\n'
          f'| Users: {len([member for member in bot.users if not member.bot])}\n'
          f'| Base OAuth URL: {utils.oauth_url(bot.user.id)}\n'
          f'| Bot started in \033[92m{"%.3f" % end_time}\033[0m seconds\n'
          f'| Current Discord.py Version: {discord.__version__}\n'
          f'# ------------------------------#')


MODULES = [
    'commands',
]

for module in MODULES:
    bot.load_extension(module)

bot.run("")
