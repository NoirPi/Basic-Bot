import locale
import datetime

import discord
from discord.ext import commands

locale.setlocale(locale.LC_ALL, "en_US.utf8")
start_time = time.time()


modules = [
    'commands'
]


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.all(), case_insensitive=True)
        
        # loading extenstions
        for module in modules:
            try:
                self.load_extension(module)
            except Exception:
                print(f'{module} not loaded.')
    
    async def on_ready():
        """When the bot is ready, you don't need an event decorator."""
        self.start_time = datetime.datetime.utcnow()
        
        # changing the bot status
        await self.change_presence(status=discord.Status.online)
        
        print(f'Ready: {self.user} (ID: {self.user.id})')


basic_bot = Bot()
basic_bot.run('token')
