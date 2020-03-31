import locale
import discord
from discord.ext import commands


# noinspection PyShadowingNames
def __init__(self, bot: commands.Bot):
    self.bot = bot


locale.setlocale(locale.LC_ALL, "en_US.utf8")
bot = commands.Bot(command_prefix="!",
                   case_insensitive=True,
                   owner_id="")


@bot.event
async def on_ready():
    """Output after the Bot is fully loaded"""
    await bot.change_presence(status=discord.Status.online)
    print(f'#-------------------------------#\n'
          f'| Successfully logged in\n'
          f'#-------------------------------#\n'
          f'| Username:  {bot.user.name}\n'
          f'| User ID:   {bot.user.id}\n'
          f'| Developer: CodingSquad Team\n'
          f'| OAuth URL: {discord.utils.oauth_url(bot.user.id)}\n'
          f'# ------------------------------#')
    

MODULES = [
    'commands',
]

for module in MODULES:
    bot.load_extension(module)

bot.run("")
