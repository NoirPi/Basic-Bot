import locale
import time

import twitchio
from twitchio.ext import commands

locale.setlocale(locale.LC_ALL, "en_US.utf8")
start_time = time.time()

MODULES = [
    'commands',
]


class Bot(commands.Bot):
    def __init__(self):
        super(Bot, self).__init__(
            command_prefix="!",
            case_insensitive=True,
        )

        for module in MODULES:
            try:
                self.load_module(module)
            except Exception as e:
                print(f'{module} not loaded.')
                print("_____________________")
                print(e)

    async def on_ready(self):
        """Output after the Bot fully loaded"""
        end_time = time.time() - start_time
        print(f'#-------------------------------#\n'
              f'| Username: {self.nick}\n'
              f'| User ID: {self.user_id}\n'
              f'| Developer:  CodingSquad Team\n'
              f'| Bot started in \033[92m{"%.3f" % end_time}\033[0m seconds\n'
              f'| Current Discord.py Version: {twitchio.__version__}\n'
              f'# ------------------------------#')


BasicBot = Bot()

BasicBot.run("")
